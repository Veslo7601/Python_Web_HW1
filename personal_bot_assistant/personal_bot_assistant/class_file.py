"""Module providing a function """
import re
from collections import UserDict
from datetime import datetime
from dateutil.parser import parse

#from Abstarct_Class_Phone import ShowAll, AddRecord, FindRecord, DeleteRecord, UpdatePhone, RemovePhone, EditPhone
from Abstarct_Class_Note import AddNote, DeleteNote, EditNote
from Abstract_Class_Address import AddAdress, RemoveAddress
from Abstract_Class_Email import AddEmail, RemoveEmail
from Abstract_Class_Birthday import AddBirthday, RemoveBirthday, ShowBirthday
from Abstract_Class_Tags import AddTag, FindTag, DeleteTag
from Abstarct_Class_Sort import SortFile

class Field:
    """Class representing a default class"""
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Class representing a Name"""

class Phone(Field):
    """Class representing a Phone"""

    @property
    def value(self):
        """Getter"""
        return self.__value

    @value.setter
    def value(self, value):
        """Setter"""
        if len(str(value)) != 10:
            raise Exception ("The number does not have 10 digits")
        elif not value.isdigit():
            raise Exception ("There are extra characters in the number")
        else:
            self.__value = value

class Email(Field):
    """Class representing a Email """

    @property
    def value(self):
        """Getter"""
        return self.__value

    @value.setter
    def value(self, value):
        """Setter"""
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regex, value)):
            self.__value = value
        else:
            raise Exception("Invalid Email")

class Birthday(Field):
    """Class representing a Birthday """

    @property
    def valid_birthday(self):
        """Getter"""
        return self.__value

    @valid_birthday.setter
    def valid_birthday(self,value):
        """Setter"""
        correct = datetime.strptime(value, '%d.%m.%Y')
        if correct:
            self.__value = correct
        else:
            raise ValueError ("The date is incorrect")

class FunctionNote(AddNote, DeleteNote, EditNote):
    """Class with functions note"""
    def __init__(self):
        self.note = " "

    def command_add_note(self,value):
        """Function add note"""
        self.note = " ".join(value)    

    def command_delete_note(self):
        """Function delete note"""
        self.note = " "

    def command_edit_note(self, value):
        """Function edit note"""
        self.command_delete_note()
        self.command_add_note(value)

class FunctionAddress(AddAdress, RemoveAddress):
    """Class with functions address"""
    def __init__(self):
        self.address = " "

    def command_add_address(self, value):
        """function for adding address"""
        self.address = " ".join(value)

    def command_delete_address(self):
        """function for delete address"""
        self.address = " "

class FunctionTag(AddTag, FindTag, DeleteTag):
    """Class with functions tags"""
    def __init__(self):
        self.tags = []

    def command_add_tag(self, tags):
        """Function add teg"""
        self.tags.append(tags)

    def command_find_tag(self, value):
        """Function find teg"""
        for tag in self.tags:
            if str(tag) == str(value):
                return value

    def command_delete_tag(self, value):
        """Function delete teg"""
        target = self.command_find_tag(value)
        if target == value:
            self.tags.remove(target)
            return "Tag delete"

class FunctionBirthdate(AddBirthday, RemoveBirthday, ShowBirthday):
    """Class with functions birthday"""
    def __init__(self):
        self.birthday = " "

    def command_add_birthday(self, value):
        """function for adding birthday"""
        self.birthday = Birthday(value)

    def command_remove_birthday(self):
        """function for remove birthday"""
        self.birthday = ' '

    def command_show_birthday(self)->int:
        """function"""
        birthday = self.birthday.value
        current_date = datetime.now().date()
        birthday_date_this_year = parse(birthday, fuzzy=False).replace(year = datetime.now().year).date()
        delta = birthday_date_this_year - current_date
        # if birthdate in future current year
        if delta.days>0:
            return delta.days
        else: 
            # If birthdate in current year has passed (calculate days to next year's date)
            return (birthday_date_this_year.replace(year=current_date.year+1) - current_date).days

class FunctionEmail(AddEmail, RemoveEmail):
    """Class with functions email"""
    def __init__(self):
        self.email = []

    def command_add_email(self, value):
        """function for adding phones"""
        self.email.append(Email(value))

    def command_delete_email(self, value):
        """function for remove email"""
        find_email = self.find_email(value)
        if find_email:
            self.email.remove(find_email)
        else:
            raise ValueError()

    def find_email(self, value):
        """function for find email"""
        for email in self.email:
            if str(email) == str(value):
                return email

class FunctionPhone:
    """Class with functions phone"""
    def __init__(self):
        self.phones = []

    def add_phone(self,value):
        """function for adding phones"""
        self.phones.append(Phone(value))

    def remove_phone(self,value):
        """function for remove phones"""
        if self.find_phone(value):
            self.phones.remove(self.find_phone(value))
        else:
            raise ValueError()

    def edit_phone(self, value, value_two):
        """function for edit phones"""
        if self.find_phone(value):
            self.remove_phone(value)
            self.add_phone(value_two)
        else:
            raise ValueError()

    def find_phone(self, value):
        """function for find phones"""
        for phone in self.phones:
            if str(phone) == str(value):
                return phone

class Record(FunctionNote, FunctionAddress, FunctionTag, FunctionBirthdate, FunctionEmail, FunctionPhone):
    """Class representing a Record"""

    def __init__(self, name):
        self.name = Name(name)
        super().__init__()
        super(FunctionNote, self).__init__()
        super(FunctionAddress, self).__init__()
        super(FunctionTag, self).__init__()
        super(FunctionBirthdate, self).__init__()
        super(FunctionEmail, self).__init__()

    def __str__(self):
        return f"Contact name: {self.name.value}\n\t-phones: {'; '.join(p.value for p in self.phones)}\n\t-email: {'; '.join(p.value for p in self.email)}\n\t-address: {self.address} \n\t-birthday: {self.birthday}\n\t-note: {self.note}\n\t-tags: {self.tags}\n"

class AddressBook(UserDict):
    """Class representing a AddressBook"""

    def add_record(self,Record):
        """function for add record"""
        return super().__setitem__(Record.name.value,Record)

    def find(self,Name):
        """function for find record"""
        for key in self.data:
            if str(key) == str(Name):
                return super().__getitem__(key)
        raise NameError("Contact does not exist, enter the name of an existing contact")

    def delete(self,Name):
        """function for delete record"""
        return super().__delitem__(Name)

    def iterator(self, value):
        """Iterator"""
        #contact_list = []
        for contact in self.data.values():
            names = str(contact.name)
            if names.find(value) != -1:
                #contact_list.append(f"{contact} have word {value}")
                yield f"{contact} have word <{value}>"

            for phone in contact.phones:
                contact_phone = str(phone)
                if contact_phone.find(value) != -1:
                    #contact_list.append(f"{contact} have word {value}")
                    yield f"{contact} have word <{value}>"

    def find_note(self, value):
        """Function find note"""
        for contact in self.data.values():
            note = str(contact.note)
            if note.find(value) != -1:
                yield f"{contact} have note <{note}>"

    def search_notes_by_tag(self, tags):
        """Function search tags"""
        for contact in self.data.values():
            for tag in contact.tags:
                if tags in tag:
                    yield f"{contact} have tag <{tags}>"

#The file ends
