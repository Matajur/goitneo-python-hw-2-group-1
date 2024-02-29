"""Module providing a function to display a list of colleagues with upcoming birthdays"""

import calendar
from collections import defaultdict
from datetime import datetime

MIN_AGE = 18  # years
MAX_AGE = 70  # years
TODAY = datetime.now().date()
TIME_SPAN = 7  # days


def check_user(user: dict[str, datetime]) -> bool:
    """
    User data verification function.

    :param user: a dictionary with user data
    :return: True if the data is valid, otherwise False
    """
    result = False
    try:
        if (365 * MIN_AGE) < (TODAY - user["birthday"].date()).days < (365 * MAX_AGE):
            if user["name"]:
                result = True
    except (AttributeError, KeyError, SyntaxError):
        pass
    return result


def get_birthdays_per_week(users_list: list[dict[str, datetime]]) -> None:
    """
    Function to create and print a list of colleagues with upcoming birthdays.

    :param users_list: a list of dictionaries with users and their birthdays
    :return: None, the function prints upcoming birthdays using an external function
    """
    birthday_people = defaultdict(list)

    for user in users_list:
        # remove users with an inappropriate age
        if check_user(user):
            birthday = user["birthday"].date()
            try:
                next_birthday = birthday.replace(year=TODAY.year)
            except ValueError:  # when birthday on February 29
                next_birthday = birthday.replace(year=TODAY.year, month=3, day=1)
            if TODAY.month == 12 and birthday.month == 1:  # for New Year's Eve
                next_birthday = next_birthday.replace(year=TODAY.year + 1)
            if 0 <= (next_birthday - TODAY).days < TIME_SPAN:
                if next_birthday.weekday() in (5, 6) and TODAY.weekday() != 0:
                    birthday_people[0].append(user["name"])
                else:
                    birthday_people[next_birthday.weekday()].append(user["name"])

    # sort defaultdict by numbers of weekdays
    birthday_people = dict(sorted(birthday_people.items()))
    print_birthdays(birthday_people)


def print_birthdays(birthday_people: dict) -> None:
    """
    Function to display a collection of colleagues with upcoming birthdays.

    :param birthday_people: a dictionary of weekdays and users with upcoming birthdays
    :return: None, the function prints upcoming birthdays
    """
    if not birthday_people:
        print("No upcoming birthdays")
    else:
        # check if there are birthdays this week
        if max(birthday_people.keys()) >= TODAY.weekday():
            print("Upcoming birthdays this week:")
            for day, value in birthday_people.items():
                if day >= TODAY.weekday():
                    print(f"{calendar.day_name[day]}: {', '.join(value)}")  # type: ignore
        # check if there are birthdays next week
        if min(birthday_people.keys()) < TODAY.weekday():
            print("Upcoming birthdays next week:")
            for day, value in birthday_people.items():
                if day < TODAY.weekday():
                    print(f"{calendar.day_name[day]}: {', '.join(value)}")  # type: ignore


if __name__ == "__main__":

    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Dummy User VIII", "birthday": datetime(1990, 2, 23)},
        {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
        {"name": "Johnny Cash", "birthday": datetime(1932, 2, 26)},
        {"name": "Wenceslas IV of Bohemia", "birthday": datetime(1361, 2, 26)},
        {"name": "Dummy User", "birthday": datetime(2000, 2, 26)},
        {"name": "Another Dummy User", "birthday": datetime(1970, 2, 22)},
        {"name": "Dummy User III", "birthday": datetime(2050, 2, 26)},
        {"name": "Dummy User IV", "birthday": datetime(1960, 1, 26)},
        {"name": "", "birthday": datetime(1960, 1, 26)},
        {"name": "Dummy User V", "birthday": 1},
        {"name": "Dummy User VI"},
        {"name": "Dummy User VII", "birthday": datetime(1990, 2, 22)},
    ]

    get_birthdays_per_week(users)
