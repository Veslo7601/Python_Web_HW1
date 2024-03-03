from abc import ABC, abstractclassmethod

class AddAdress(ABC):
    @classmethod
    @abstractclassmethod
    def command_add_address(self):
        pass

class RemoveAddress(ABC):
    @classmethod
    @abstractclassmethod
    def command_remove_address(self):
        pass
    