import json

def read_users() -> list[str]:
    with open("./data/users.json", 'r') as users_file:
        user_list: list = json.load(users_file).get("users", [])

    return user_list


def read_entries() -> list[dict]:
    with open("./data/entries.json", 'r') as entries_file:
        entry_list: list = json.load(entries_file).get("entries", [])

    return entry_list