from .trello_command_abc import TrelloCommand
from datetime import datetime
import calendar


class CompleteRegularDailyTasks(TrelloCommand):
    """
    Command move all regular daily tasks to list with completed tasks.
    """
    command_name = 'complete_day'
    CURRENT_WEEKDAY = list(calendar.day_name)[datetime.today().weekday()]
    DONE_LIST_NAME = "Done"
    HABITS_LIST_NAME = 'Habits/Routines'

    def execute(self):
        today_tasks_list = self.trello_client.get_weekly_tasks_list(self.CURRENT_WEEKDAY)
        done_tasks_list = self.trello_client.get_yearly_tasks_list(self.DONE_LIST_NAME)
        standard_tasks = self._filter_tasks(today_tasks_list.list_cards())
        self._complete_tasks(done_tasks_list, standard_tasks)

    def _filter_tasks(self, tasks_list):
        tasks_list = list(filter(lambda card: not self._is_habit(card), tasks_list))
        return tasks_list

    def _is_habit(self, habit_card): # Should be optimized
        habits_list = self.trello_client.get_yearly_tasks_list(self.HABITS_LIST_NAME)
        all_habit_card_names = [card.name for card in habits_list.list_cards()]
        return habit_card.name in all_habit_card_names

    def _complete_tasks(self, done_tasks_list, standard_tasks):
        current_year_board = self.trello_client.get_current_year_board()
        for card in standard_tasks:
            card.change_board(board_id=current_year_board.id)
            card.change_list(list_id=done_tasks_list.id)




