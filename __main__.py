from command_factory import TrelloCommandsFactory
import sys

try:
    command = TrelloCommandsFactory()
    trello_command = command.create_instance(sys.argv[1])
    trello_command.execute()
except IndexError:
    print("Here is example of script usage: >>>'python trello_api <command_name>'")









