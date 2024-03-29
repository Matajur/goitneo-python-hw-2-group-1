"""Module providing a functionality to manage the contacts in a contact list"""

from source.classes import (
    NameValidationError,
    PhoneIndexError,
    PhoneValidationError,
    RecordValidationError,
    Record,
    Name,
    Phone,
    AddressBook,
)


def input_error(func) -> str:
    """
    A decorator to handle input errors.

    :param func: function where an input error can occur
    :return: function if no input error occurred, or a description of the error
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide name and phone."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Provide contact name."
        except TypeError:
            return "Provide contact name."
        except NameValidationError:
            return "The name must contain at least 3 characters."
        except PhoneIndexError:
            return "There is no such phone number in the record."
        except PhoneValidationError:
            return "Wrong phone number format, should be 10 digits, ex. 1234567890"
        except RecordValidationError:
            return "A contact with that name already exists."

    return inner


@input_error
def add_contact(book: AddressBook, *args: list) -> str:
    """
    Function of adding a new contact with a phone to the contact list.
    A contact can be created without a phone number.

    :param book: a dictionary with user contacts
    :param args: list with contact name and phone number to add to contact list
    :return: a new record
    """
    name, *phones = args
    record = Record(Name(name))
    if phones:
        for phone in phones:
            record.add_phone(Phone(phone))
    book.add_record(record)
    return f"New: {record}."


@input_error
def add_phone(book: AddressBook, *args: list) -> str:
    """
    Function of adding a new phone or phones to the existing record in contact book.

    :param book: a dictionary with user contacts
    :param args: a list with the contact name and new phone numbers to add
    :return: an updated record
    """
    name, *phones = args
    record = book.find(name)
    for phone in phones:
        record.add_phone(Phone(phone))
    return f"Displaying: {record}."


@input_error
def edit_phone(book: AddressBook, *args: list) -> str:
    """
    Function of changing an existing contact's phone number.

    :param book: a dictionary with user contacts
    :param args: a list with the contact name, the old phone number to replace, 
                and the new phone number
    :return: an updated record
    """
    name, *phones = args
    record = book.find(name)
    record.edit_phone(phones)
    return f"Updated: {record}."


@input_error
def find_contact(book: AddressBook, *args: list) -> str:
    """
    Function of displaying the user's contact.

    :param book: a dictionary with user contacts
    :param args: a list with contact name
    :return: a record from the address book
    """
    name = args[0]
    return book.find(name)


@input_error
def find_phone(book: AddressBook, *args: list) -> str:
    """
    Function of changing an existing contact's phone number.

    :param book: a dictionary with user contacts
    :param args: a list with the contact name and the phone number to find
    :return: a message with the contact name and phone number found
    """
    name, *phones = args
    record = book.find(name)
    index = record.find_phone(phones[0])
    return f"{record.name}: {record.phones[index]}."


def greetings(*_) -> str:
    """
    User greeting function.

    :return: a message with greetings
    """
    return "How can I help you?"


@input_error
def remove_contact(book: AddressBook, *args: list) -> str:
    """
    Function to erase an existing contact.

    :param book: a dictionary with user contacts
    :param args: a list with contact name to be erased
    :return: a message about a successful operation
    """
    name = args[0]
    book.delete(name)
    return f"Contact: {name} removed."


@input_error
def remove_phone(book: AddressBook, *args: list) -> str:
    """
    Function of changing an existing contact's phone number.

    :param book: a dictionary with user contacts
    :param args: a list with the contact name and the phone number to delete
    :return: an updated record
    """
    name, *phones = args
    record = book.find(name)
    record.remove_phone(phones[0])
    return f"Updated: {record}."


def show_contacts(book: AddressBook, *_) -> str:
    """
    Function of displaying a complete list of contacts.

    :param book: a dictionary with user contacts
    :return: a string with the full contact list or a warning that the
            contact list is empty
    """
    if len(book):
        contacts = dict(sorted(book.items()))
        result = "Contact list:"
        for _, record in contacts.items():
            result += f"\n{record}"
        return result
    return "Contact list is empty."
