from abc import ABC, abstractclassmethod

class class_hello(ABC):

    @classmethod
    @abstractclassmethod
    def command_hello(self):
        pass

class class_start_save(ABC):

    @classmethod
    @abstractclassmethod
    def start(self):
        pass

    @classmethod
    @abstractclassmethod
    def save(self):
        pass

