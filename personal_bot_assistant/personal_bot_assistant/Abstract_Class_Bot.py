from abc import ABC, abstractclassmethod

class Hello(ABC):

    @classmethod
    @abstractclassmethod
    def command_hello(self):
        pass

class StartSave(ABC):

    @classmethod
    @abstractclassmethod
    def start(self):
        pass

    @classmethod
    @abstractclassmethod
    def save(self):
        pass

class GoodBye(ABC):
    @classmethod
    @abstractclassmethod
    def command_good_bye(self):
        pass

class Help(ABC):
    @classmethod
    @abstractclassmethod
    def command_help_info(self):
        pass