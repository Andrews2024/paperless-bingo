import json
from flask import Flask, redirect, render_template, request

from helper import read_users, read_entries
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return render_template("home.html", user_list = read_users(),
                            entry_list = read_entries())

@app.route('/add-user', methods = ['POST'])
def add_user():
    # Get name to add and list to add to
    name = request.form.get('name')
    user_list = read_users()

    with open("./data/users.json", 'w') as users_file:
        if name not in user_list:
            # Add user to list if it's unique
            user_list.append(name)

        # Save list back to JSON
        json.dump({"users": user_list}, users_file)

    return redirect('/')

@app.route('/add-entry', methods = ['POST'])
def add_entry():
    # Get name to add and list to add to
    name = request.form.get('dropdown')
    event = request.form.get('event')
    user_list = read_users()
    entry_list = read_entries()

    with open("./data/entries.json", 'w') as entry_file:
        # Add entry to list
        entry = {"name": name, "event": event}
        if entry not in entry_list:
            entry_list.append(entry)
        
        # Save list back to JSON
        json.dump({"entries": entry_list}, entry_file)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
