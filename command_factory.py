import commands
from inspect import getmembers, isclass, isabstract


class TrelloCommandsFactory(object):
    trello_commands = {}

    def __init__(self):
        self._load_commands()

    def _load_commands(self):
        classes = getmembers(commands, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, commands.TrelloCommand) and _type is not commands.TrelloCommand:
                if _type is not commands.NoCommand and getattr(_type, 'command_name') is None:
                    raise NotImplementedError(
                        "class variable 'command_name' should be implemented in class {}".format(_type.__name__))
                self.trello_commands.update([[_type.command_name, _type]])

    def create_instance(self, command_name):
        if command_name in self.trello_commands:
            return self.trello_commands[command_name]()
        else:
            return commands.NoCommand(self.trello_commands)
