"""
Project: Daily Planner 1 (Pre OOP)

Author: Daniel Jeon
Website: https://github.com/danielljeon/basics_of_python

The purpose of this project is to make a daily planner that uses everything a beginner python
programmer will probably know up to (PRIOR TO) OOP and including python packages.

Important aspects of programming that this project covers:
- Variables
- Functions
- Loops
- Iterables
- Packages

Note:
    The point of this project code is not to necessarily have the most efficient or correct answer,
    but rather the method that most beginner coders would best understand. This project is to teach
    and reinforce concepts of python coding in a fun and interactive way.
"""

from apscheduler.schedulers.background import BackgroundScheduler  # Scheduling package
from datetime import datetime
import dateutil.parser as dparser
import json  # JSON is for long term storage of the user's specified

USER_NAME = "Daniel"
DEFAULT_JSON_FILE_PATH = "reminders.json"

print(f"-------------------- {USER_NAME}'s Daily Planner --------------------")


def create_new_reminder(
    name: str, remind_at: list[str], details: str = ""
) -> dict[str, str | list[datetime]]:
    # Extract the datetime from strings which specify reminder notification datetime.
    datetime_list = []
    for r in remind_at:
        extracted_datetime = dparser.parse(r, fuzzy=True, dayfirst=False)
        datetime_list.append(extracted_datetime)

    # The same code above but with list comprehension.
    # datetime_list = [dparser.parse(r, fuzzy=True, dayfirst=False) for r in remind_at]

    return {"name": name, "remind_at": datetime_list, "details": details}


def print_reminder(reminder: dict[str, str | list[datetime]]):
    current_datetime = datetime.now().strftime("%b %d, %Y - %H:%M:%S")
    print_header = f"---------- {reminder.get('name')} ----------"
    print_footer = "-" * len(print_header)

    print(
        f"{print_header}\n" f"{current_datetime}\n" f"{reminder.get('details')}\n" f"{print_footer}"
    )


def save_reminders_to_json(
    reminders: list[dict[str, str | list[datetime]]], filepath: str = DEFAULT_JSON_FILE_PATH
):
    def datetime_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    # Ensure file extension is present.
    if filepath[-5:] != ".json":
        filepath += ".json"

    # Write the provided reminders to the json file.
    with open(filepath, "w") as file:
        json.dump(reminders, file, default=datetime_serializer, indent=4)


# def read_reminders_from_json(
#     filepath: str = DEFAULT_JSON_FILE_PATH,
# ) -> list[dict[str, str | list[datetime]]]:
#     def datetime_deserializer(dct):
#         if "__datetime__" in dct:
#             return datetime.fromisoformat(dct["__datetime__"])
#         return dct
#
#     # Read reminders from the provided json file.
#     with open(filepath, "r") as file:
#         reminders = json.load(file, object_hook=datetime_deserializer)
#
#     return reminders


def add_reminder_to_scheduler(
    scheduler: BackgroundScheduler, reminder: dict[str, str | list[datetime]]
):
    remind_at_datetimes = reminder.get("remind_at")

    for dt in remind_at_datetimes:
        scheduler.add_job(print_reminder, args=[reminder], trigger="date", run_date=dt)


def main():
    # Create a scheduler.
    scheduler = BackgroundScheduler()
    scheduler.start()

    all_reminders = []

    # STEP 1:
    reminder = create_new_reminder(
        name="Sleep", remind_at=["2023-08-01 00:38:40"], details="Go to sleep!!!"
    )
    all_reminders.append(reminder)

    # STEP 2:
    add_reminder_to_scheduler(scheduler=scheduler, reminder=reminder)

    # STEP 3:
    save_reminders_to_json(reminders=all_reminders, filepath="MyReminders.json")

    try:
        # Keep the script running while the scheduler is active.
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler gracefully when the script is interrupted.
        scheduler.shutdown()


if __name__ == "__main__":
    main()
