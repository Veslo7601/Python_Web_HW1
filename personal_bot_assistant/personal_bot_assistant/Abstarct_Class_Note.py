
from abc import ABC, abstractclassmethod

class AddNote(ABC):
    @classmethod
    @abstractclassmethod
    def command_add_note(self):
        pass

class DeleteNote(ABC):
    @classmethod
    @abstractclassmethod
    def command_delete_note(self):
        pass

class EditNote(ABC):
    @classmethod
    @abstractclassmethod
    def command_edit_note(self):
        pass

class FindNote(ABC):
    @classmethod
    @abstractclassmethod
    def command_find_note(self):
        pass
