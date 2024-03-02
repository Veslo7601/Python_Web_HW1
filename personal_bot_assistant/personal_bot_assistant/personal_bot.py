"""Module providing a function """
import pickle
import os
import shutil
from collections import UserDict
from datetime import datetime
from class_file import AddressBook, Record
from class_command_bot import class_hello, class_show_all

#from abc import ABC, abstractclassmethod

def decorator(func):
    """Decorator"""
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "Enter the correct command"
        except ValueError:
            return "Enter correct command"
        except IndexError:
            return "Enter the correct command, name and phone number"
        except NameError as e:
            return f"{e}"
        except FileNotFoundError:
            global book
            book = AddressBook()
            with open('Data.bin', 'wb') as file:
                pickle.dump(book, file)
                return "Create Data"
        except Exception as e:
            return f"{e}"
    return wrapper


class Bot(class_hello):
    """   """
    def command_hello(self):
        """Function Hello"""
        return "How can I help you?"

    @decorator
    def start(self):
        """Load data"""
        with open('Data.bin', 'rb') as file:
            global book
            book = pickle.load(file)
        return "Bot start"

    def save(self):
        """Save data"""
        global book
        with open('Data.bin', 'wb') as file:
            pickle.dump(book, file)

    def command_good_bye(self):
        """Function close bot"""
        global ACTIVE_BOT
        ACTIVE_BOT = False
        return "Good Bye!"

class BotPhone(class_show_all):
    """A class for phone number management"""
    def command_show_all(self):
        """Function show all phone number"""
        for contact in book.values():
            print(f'{contact}')

    def command_add_record(self, name, phone):
        """Adding a contact to the Address Book"""
        new_record = Record(name)
        new_record.add_phone(phone)
        book.add_record(new_record)
        return "Contact added successfully"

    def command_find_record(self, value):
        """Find a contact in the Address Book"""
        for i in book.iterator(value):
            print(i)

    def command_delete_record(self, name):
        """Deleting a contact in the Address Book"""
        if book.find(name):
            book.delete(name)
            return f"Contact {name} deleted"

    def command_update_phone(self, name,phone):
        """Adding a phone number"""
        if book.find(name):
            new_phone = book.find(name)
            new_phone.add_phone(phone)
            return new_phone

    def command_remove_phone(self, name, phone):
        """Deleting a phone number"""
        if book.find(name):
            record = book.find(name)
            record.remove_phone(phone)
            return record

    def command_edit_phone(self, name,phone_one,phone_two):
        """Changing the phone number"""
        if book.find(name):
            record = book.find(name)
            record.edit_phone(phone_one,phone_two)
            return record

class BotNote():
    """A class for note management"""
    def command_add_note(self, name, note):
        """Function add note"""
        if book.find(name):
            record = book.find(name)
            record.add_note(note)
            return "Note added successfully"

    def command_delete_note(self, name):
        """Function delete note"""
        record = book.find(name)
        if record:
            record.delete_note()
            return "Note delete"

    def command_edit_note(self, name, note):
        """Function edit note"""
        record = book.find(name)
        if record:
            record.edit_note(note)
            return "Note edit"

    def command_find_note(self, value):
        """Function find note"""
        for i in book.find_note(value):
            print(i)

def command_add_address(name, address):
    """Adding a address"""
    if book.find(name):
        new_address = book.find(name)
        new_address.add_address(address)
        return "Address added successfully"

def command_add_email(name, email):
    """Adding a email"""
    if book.find(name):
        new_email = book.find(name)
        new_email.add_email(email)
        return "Email added successfully"

def command_add_birthday(name, birthday):
    """Adding a birthday"""
    if book.find(name):
        new_birthday = book.find(name)
        new_birthday.add_birthday(birthday)
        return "Birthday added successfully"

def command_show_birthday(days: int):
    cnt = 0
    for contact in book.values():
        if contact.days_to_birthday() - int(days) == 0:
            print(f'{contact}')
            cnt += 1
    if cnt > 0:
        return f"Contacts that have birthday in {days} days are printed above"
    else:
        return f"There are no contacts that have birthdays in {days} days in the AddressBook"
        

def command_help_info():
    return """Commands list:\n
        *hello - prints greeting \n
        *add <contact name> <phone number>- adds record if contact name is not present, adds phone if contact name is present and phone number differs from other \n
        *update <contact name> <old phone> <new phone>- changes contact phone by name \n
        *delete <contact name>- delete contact or delete \n
        *remove <contact name> <phone> - delete specified phone for the contact \n        
        *show all - prints entire Address Book \n
        *find <name or phone> - filter by name letters or phone number \n
        *exit, good bye, close - saves changes to database and exit \n
        *add-address <name, address> - adds address for the contact with specified name \n
        *add-email <name, email> - adds email for the specified contact \n
        *add-birthday <name, borthday> - adds birthday for the specified contact \n
        *write <name, note> - adds note for the contact with specified name \n
        *delete-note <name, note> - removes note for the contact with specified name \n
        *edit-note <name, note> - edit note \n
        *find-note <note> - find contact with specified note \n
        *show-birthdate <number of days> - shows all contacts wich have birthday on a date that will occure in specified number of days \n
        *sort <folder path> - sorts the files in the specified folder\n
        *add-tag <name, tag> - adds a tag to the specified contact\n
        *find-tag <tag> - searches for contacts by the specified tags\n"""

def command_remove_address(name, address):
    """Deleting a address"""
    if book.find(name):
        record = book.find(name)
        record.remove_address(address)
        return 'Address deleting'

def command_remove_email(name, email):
    """Deleting a email"""
    if book.find(name):
        record = book.find(name)
        record.remove_email(email)
        return 'Email deleting'

def command_remove_birthday(name):
    """Deleting a birthday"""
    if book.find(name):
        record = book.find(name)
        record.remove_birthday()
        return 'Birthda deleting'

def sort_files_by_category(folder_path):
    """Function sort files by category"""
    if not os.path.exists(folder_path):
        return "The path does not exist."

    categories = {
        'image': ['.jpg', '.jpeg', '.png', '.gif'],
        'video': ['.mp4', '.avi', '.mkv'],
        'documents': ['.pdf', '.doc', '.docx', '.txt'],
        'other': []  
    }

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_name)
            found_category = False
            for category, extensions in categories.items():
                if file_extension.lower() in extensions:
                    found_category = True
                    category_folder = os.path.join(folder_path, category)
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    shutil.move(file_path, os.path.join(category_folder, file_name))
                    break
            if not found_category:
                other_folder = os.path.join(folder_path, 'інше')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, file_name))

    return "Sorting is complete!"

def command_add_teg(name, tags):
    """Adding a tags"""
    if book.find(name):
        new_tags = book.find(name)
        new_tags.add_teg(tags)
        return "Tags added successfully"
    
def command_find_teg(value):
    """Function find teg"""
    for i in book.search_notes_by_tag(value):
        print(i)


def get_command(command):
    """Function command bot"""
    command_list = {
        #"hello": command_hello,
        "hello": bot.command_hello,

        "show all": phone.command_show_all,
        "add": phone.command_add_record,
        "find": phone.command_find_record,
        "delete": phone.command_delete_record,

        "update" : phone.command_update_phone,
        "remove": phone.command_remove_phone,
        "edit": phone.command_edit_phone,

        "good bye": bot.command_good_bye,
        "close": bot.command_good_bye,
        "exit": bot.command_good_bye,

        "add-address": command_add_address,
        "add-email": command_add_email,
        "add-birthday": command_add_birthday,

        "write": note.command_add_note,
        "delete-note": note.command_delete_note,
        "edit-note": note.command_edit_note,
        "find-note": note.command_find_note,

        "remove-address": command_remove_address,
        "remove-email": command_remove_email,
        "remove-birthday": command_remove_birthday,

        "sort": sort_files_by_category,
        "add-tag": command_add_teg,
        "find-tag": command_find_teg,

        "show-birthdate": command_show_birthday,
        "help": command_help_info,
    }

    return command_list[command]

ACTIVE_BOT = False
book = None

bot = Bot()
phone = BotPhone()
note = BotNote()

@decorator
def command_parser(user_input):
    """Сommand parser"""
    if user_input in ["show all", "hello", "good bye", "close", "exit", "help"]:
        return get_command(user_input)()
    else:
        user_input = user_input.split()
        if user_input[0] in ["phone", "delete", "find", "delete-note", "find-note", "show-birthdate", "remove-birthday", "sort","find-tag",]:
            return get_command(user_input[0])(user_input[1])
        if user_input[0] in ["remove", "update", "add", "add-email", "add-birthday", "remove-address", "remove-email", "add-tag"]:
            return get_command(user_input[0])(user_input[1],(user_input[2]))
        if user_input[0] in ["write","add-address", "edit-note"]:
            return get_command(user_input[0])(user_input[1],(user_input[2:]))
        if user_input[0] in ["edit"]:
            return get_command(user_input[0])(user_input[1],(user_input[2]),(user_input[3]))
        raise ValueError()

def main():
    """Bot"""
    print(bot.start())
    global ACTIVE_BOT
    ACTIVE_BOT = True
    while ACTIVE_BOT:
        user_input = input("Enter the command: ").lower().strip()
        print(command_parser(user_input))
        print("____________________________________")
        bot.save()

if __name__ == '__main__':
    main()

#The file ends
