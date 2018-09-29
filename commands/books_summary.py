from .trello_command_abc import TrelloCommand


class BooksSummary(TrelloCommand):
    """
    Command print yearly books summary. Amount read and amount planned.
    """
    command_name = 'books_summary'
    EDUCATION_TASKS_LIST = "Education & Skills Development"

    def execute(self):
        today_tasks_list = self.trello_client.get_yearly_tasks_list(self.EDUCATION_TASKS_LIST)
        task_card = BooksSummary.find_card(today_tasks_list)
        checklists = task_card.checklists
        plan_to_read = sum(len(check_list.items) for check_list in checklists)
        red_books = sum(
            len(list(filter(lambda x: x.get('state') == 'complete', check_list.items))) for check_list in checklists
            )
        print("You have read {} books out of {} planned this year.".format(red_books, plan_to_read))

    @staticmethod
    def find_card(cards_list):
        card_name_part = 'Books'
        searched_card = None
        for card in cards_list.list_cards():
            if card_name_part in card.name:
                searched_card = card
                break
        return searched_card
