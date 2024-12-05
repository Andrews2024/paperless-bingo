import json
from flask import flash

def read_users() -> list[str]:
    with open("./data/users.json", 'r') as users_file:
        user_list: list = json.load(users_file).get("users", [])

    return user_list


def read_entries() -> list[dict]:
    with open("./data/entries.json", 'r') as entries_file:
        entry_list: list = json.load(entries_file).get("entries", [])

    return entry_list


def sort_entries(filter_name: str) -> tuple(list[dict]):
    entry_list = read_entries()
    free_entries = []
    named_entries = []

    # Get free space options and options where name != filter name
    for entry in entry_list:
        if entry.get("name") == "free space":
            free_entries.append(entry)
        elif entry.get("name") == filter_name:
            continue
        else:
            named_entries.append(entry)
    
    # Return free spaces, names spaces
    return free_entries, named_entries

def validate_enough_options(free_entries: list[dict], named_entries: list[dict]) -> bool:
    enough_options = True

    # Check for number of free spaces
    if len(free_entries) < 1:
        flash("Need at least one entry as free space.")
        enough_options = False

    if len(named_entries) < 24:
        flash("Need at least 24 entries that are not associated with given user name.")
        enough_options = False
    
    return enough_options