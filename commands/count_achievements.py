from commands.trello_command_abc import TrelloCommand


class CountAchievements(TrelloCommand):
    """
    Command count all cards that marked as my personal achievements and print total number.
    """
    command_name = 'count_achievements'
    LIST_NAME = "Achievements"

    def execute(self):
        achievements_list = self.trello_client.get_yearly_tasks_list(self.LIST_NAME)
        total_achievements_num = len(achievements_list.list_cards())
        if total_achievements_num == 0:
            print("Unfortunately you have {} achievements this year ! :( ".format(total_achievements_num))
        elif total_achievements_num < 5:
            print("You are doing progress, you have {} achievements this year ! Keep moving !".format(
                total_achievements_num))
        elif total_achievements_num >= 5:
            print("Congratulations, you have {} achievements this year !".format(total_achievements_num))
