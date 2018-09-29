from trello import TrelloClient
import os
from requests.exceptions import ConnectionError

from commands.exceptions import BoardNotFoundException, ListNotFoundException


class TrelloAPI(object):
    TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
    MY_TOKEN = os.getenv('MY_TOKEN')
    TOKEN_SECRET = os.getenv('TOKEN_SECRET')
    CURRENT_YEAR_BOARD_NAME = 'My 2018 Goals (Year of Canada career and life enhancement )' ## Rename it
    WEEKLY_PLANNING_BOARD_NAME = 'Weekly Planning'

    def __init__(self):
        try:
            self.client = TrelloClient(
                api_key=self.TRELLO_API_KEY,
                api_secret='your-secret',
                token=self.MY_TOKEN,
                token_secret=self.TOKEN_SECRET
            )
            self.all_current_year_lists = self._map_all_current_year_lists()
            self.all_week_lists = self._map_all_week_lists()
        except ConnectionError:
            print("There is a problem with internet connection")

    def _map_all_current_year_lists(self):
        board = self.get_current_year_board()
        board_name_to_id = {i.name: i for i in board.all_lists()}
        return board_name_to_id

    def _map_all_week_lists(self):
        board = self.get_my_week_board()
        board_name_to_id = {i.name: i for i in board.all_lists()}
        return board_name_to_id

    def get_yearly_tasks_list(self, list_name):
        if list_name in self.all_current_year_lists:
            return self.all_current_year_lists[list_name]
        else:
            current_board = self.get_current_year_board()
            tasks_list = TrelloAPI.get_list_by_name(board=current_board, list_name=list_name)
            return tasks_list

    def get_current_year_board(self):
        for board in self.get_boards():
            if board.name == self.CURRENT_YEAR_BOARD_NAME:
                return board
        raise BoardNotFoundException(('We cant find {} board.'.format(self.CURRENT_YEAR_BOARD_NAME)))

    def get_weekly_tasks_list(self, list_name):
        if list_name in self.all_week_lists:
            return self.all_week_lists[list_name]
        else:
            current_board = self.get_my_week_board()
            tasks_list = TrelloAPI.get_list_by_name(board=current_board, list_name=list_name)
            return tasks_list

    def get_my_week_board(self):
        for board in self.get_boards():
            if board.name == self.WEEKLY_PLANNING_BOARD_NAME:
                return board
        raise BoardNotFoundException('We cant find {} board.'.format(self.WEEKLY_PLANNING_BOARD_NAME))

    def get_boards(self):
        return self.client.list_boards()

    @staticmethod
    def get_list_by_name(board, list_name):
        board_name_to_id = {i.name: i for i in board.all_lists()}
        trello_list = board_name_to_id.get(list_name)
        if trello_list is None:
            raise ListNotFoundException("We can't find list {} in board {} !".format(list_name, board.name))
        return trello_list



