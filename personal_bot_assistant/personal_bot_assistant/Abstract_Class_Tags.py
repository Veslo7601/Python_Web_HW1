from abc import ABC, abstractclassmethod

class AddTag(ABC):
    @classmethod
    @abstractclassmethod
    def command_add_tag(self):
        pass

class FindTag(ABC):
    @classmethod
    @abstractclassmethod
    def command_find_tag(self):
        pass

class DeleteTag(ABC):
    @classmethod
    @abstractclassmethod
    def command_delete_tag(self):
        pass