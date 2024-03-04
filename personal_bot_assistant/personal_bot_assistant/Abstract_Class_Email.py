from abc import ABC, abstractclassmethod

class AddEmail(ABC):
    @classmethod
    @abstractclassmethod
    def command_add_email(self):
        pass

class RemoveEmail(ABC):
    @classmethod
    @abstractclassmethod
    def command_delete_email(self):
        pass