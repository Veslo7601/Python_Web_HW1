from abc import ABC, abstractclassmethod

class AddBirthday(ABC):
    @classmethod
    @abstractclassmethod
    def command_add_birthday(self):
        pass

class RemoveBirthday(ABC):
    @classmethod
    @abstractclassmethod
    def command_remove_birthday(self):
        pass

class ShowBirthday(ABC):
    @classmethod
    @abstractclassmethod
    def command_show_birthday(self):
        pass