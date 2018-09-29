from commands.api import TrelloAPI
from commands.command_abc import AbstractCommand
import abc


class TrelloCommand(AbstractCommand):
    __metaclass__ = abc.ABCMeta
    command_name = None

    def __init__(self):
        self.trello_client = TrelloAPI()


