"""Module providing a console bot assistant with CLI"""

from source.functions import (
    add_contact,
    add_phone,
    edit_phone,
    find_phone,
    greetings,
    remove_contact,
    remove_phone,
    find_contact,
    show_contacts,
)
from source.classes import AddressBook


commands = {
    "add": add_contact,
    "all": show_contacts,
    "append": add_phone,
    "edit": edit_phone,
    "hello": greetings,
    "phone": find_phone,
    "delete": remove_phone,
    "remove": remove_contact,
    "show": find_contact,
}


def parse_input(user_input: str) -> tuple[str, *tuple[str, ...]]:
    """
    Function to parse commands received from the user using the CLI.

    :param user: a string with a command and possible arguments
    :return cmd, *args: a tuple with a command in string format and
                        the arguments, if any, as a tuple of strings
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main() -> None:
    """
    Function that provides Command Line Interface.
    """
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command not in commands:
            print("Invalid command.")
        else:
            print(commands[command](book, *args))


if __name__ == "__main__":
    main()
