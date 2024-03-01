from abc import ABC, abstractclassmethod

class class_hello(ABC):

    @classmethod
    @abstractclassmethod
    def command_hello(self):
        pass

class class_show_all(ABC):

    @classmethod
    @abstractclassmethod
    def command_show_all(self):
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




class bot:
    class phone:
        pass

    class email:
        pass

    class addres:
        pass

    class note:
        pass

    class pasrser:
        pass
