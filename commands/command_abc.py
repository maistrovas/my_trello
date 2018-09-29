import abc


class AbstractCommand(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass
