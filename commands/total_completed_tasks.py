from commands.trello_command_abc import TrelloCommand


class NumYearlyCompletedTasks(TrelloCommand):
    """
    Command count and print all yearly completed tasks summary
    """
    command_name = 'total_completed'
    LIST_NAME = "Done"

    def execute(self):
        completed_tasks_list = self.trello_client.get_yearly_tasks_list(self.LIST_NAME)
        num_total_completed = len(completed_tasks_list.list_cards())
        print("You have completed {} tasks this year !".format(num_total_completed))
