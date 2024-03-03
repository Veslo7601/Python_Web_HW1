from abc import ABC, abstractclassmethod

class SortFile(ABC):
    @classmethod
    @abstractclassmethod
    def sort_files_by_category(self):
        pass