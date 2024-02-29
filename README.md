# Homework #2

A virtual assistant with a command line interface (CLI)

## General acceptance criteria

* The repository goitneo-python-hw-1-group-name has been created.
* The homework contains a link to the GitHub repository and an attached repository file in .zip format.
* The assignments were completed precisely in accordance with the technical description (guidelines and evaluation criteria).
* There are no errors or warnings in the console when launching the bot.
* The names of variables and functions are clear and descriptive.
* The code is properly formatted and complies with the PEP8 standard.

## Task #1

### Technical description

Complete the assistant's console bot from the homework 1 and add error processing using the `input_error` decorator.

## Task #2

### Technical Description

Continue to develop the virtual assistant with a CLI interface. Develop a system to manage the address book.

#### Entities:

* `Field`: A base class for record fields.
* `Name`: A class for storing a contact name. Required field.
* `Phone`: A class for storing a phone number. Has format validation (10 digits).
* `Record`: A class for storing information about a contact, including name and contacts list.
* `AddressBook`: A class for storing and managing records.

#### Functionality:

1. `AddressBook`:
    * Adding records.
    * Search for records by name.
    * Delete records by name.
2. `Record`:
    * Adding phone numbers.
    * Deleting phone numbers.
    * Editing phone numbers.
    * Search for a phone number.

### Assessment Criteria

1. The class `AddressBook`:
    * A method `add_record` adding a record to `self.data` has been implemented.
    * A `find` method for finding a record by name has been implemented.
    * A `delete` method deleting a record by name has been implemented.
2. The class `Record`:
    * The `Name` object is stored in a separate attribute.
    * The list of `Phone` objects is stored in a separate attribute.
    * The methods for adding — `add_phone`, deleting — `remove_phone`, editing — `edit_phone`, and searching for Phone objects — `find_phone` have been implemented.
3. The class `Phone`:
    * The phone number validation has been implemented (must be `10` digits).
