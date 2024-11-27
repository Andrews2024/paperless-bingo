import json

def read_users() -> list[str]:
    with open("./data/users.json", 'r') as users_file:
        user_list: list = json.load(users_file).get("users", [])

    return user_list