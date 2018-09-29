from .command_abc import AbstractCommand


class NoCommand(AbstractCommand):

    def __init__(self, supporting_commands):
        self.supporting_commands = supporting_commands

    def execute(self):
        formatted_commands = self._format_commands()
        print("Command not found ! Here is the list of supporting commands:\n{}".format(formatted_commands))

    def _format_commands(self):
        formatted_commands = ''
        for command in self.supporting_commands.keys():
            formatted_commands += command + '\n'  # Error we have no command_name implemented
        return formatted_commands
