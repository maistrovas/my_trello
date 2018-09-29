from .trello_command_abc import TrelloCommand
from datetime import datetime, timedelta
import calendar


class CompleteDailyHabits(TrelloCommand):
    """
    Command move tasks that is my new daily habits to the next day.
    """
    command_name = 'complete_habits'
    CURRENT_WEEKDAY = list(calendar.day_name)[datetime.today().weekday()]
    NEXT_WEEKDAY = list(calendar.day_name)[(datetime.today() + timedelta(days=1)).weekday()]
    HABITS_LIST_NAME = 'Habits/Routines'

    def execute(self):
        today_tasks_list = self.trello_client.get_weekly_tasks_list(self.CURRENT_WEEKDAY)
        next_day_tasks_list = self.trello_client.get_weekly_tasks_list(self.NEXT_WEEKDAY)
        habits = self._filter_tasks(today_tasks_list.list_cards())
        CompleteDailyHabits.move_habits(next_day_tasks_list, habits)
        if len(habits) > 0:
            print("Success, we have moved {} habit tasks to next day".format(len(habits)))
        else:
            print("There are not habit tasks in your list today")

    def _filter_tasks(self, tasks_list):
        tasks_list = list(filter(lambda card: self._is_habit(card), tasks_list))
        return tasks_list

    def _is_habit(self, habit_card): # Should be optimized
        habits_list = self.trello_client.get_yearly_tasks_list(self.HABITS_LIST_NAME)
        all_habit_card_names = [card.name for card in habits_list.list_cards()]
        return habit_card.name in all_habit_card_names

    @staticmethod
    def move_habits(next_day_tasks_list, habits):
        for card in habits:
            card.change_list(list_id=next_day_tasks_list.id)
