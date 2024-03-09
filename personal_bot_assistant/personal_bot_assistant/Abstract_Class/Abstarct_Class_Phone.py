from abc import ABC, abstractclassmethod

class ShowAll(ABC):
    """Abstract class """
    @classmethod
    @abstractclassmethod
    def command_show_all(self):
        """Abstract function """
        pass

class AddRecord(ABC):
    """Abstract class """
    @classmethod
    @abstractclassmethod
    def command_add_record(self):
        """Abstract function """
        pass

class FindRecord(ABC):
    """Abstract class """
    @classmethod
    @abstractclassmethod
    def command_find_record(self):
        """Abstract function """
        pass

class DeleteRecord(ABC):
    """Abstract class """
    @classmethod
    @abstractclassmethod
    def command_delete_record(self):
        """Abstract function """
        pass

class UpdatePhone(ABC):
    """Abstract class """
    @classmethod
    @abstractclassmethod
    def command_update_phone(seld):
        """Abstract function """
        pass

class RemovePhone(ABC):
    """Abstract class """
    @classmethod
    @abstractclassmethod
    def command_remove_phone(self):
        """Abstract function """
        pass

class EditPhone(ABC):
    """Abstract class """
    @classmethod
    @abstractclassmethod
    def command_edit_phone(self):
        """Abstract function """
        pass