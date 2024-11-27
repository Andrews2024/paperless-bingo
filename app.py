import json
from flask import Flask, redirect, render_template, request

from helper import read_users
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello():
    return render_template("home.html", user_list = read_users())

@app.route('/add-user', methods = ['POST'])
def add_user():
    # Get name to add and list to add to
    name = request.form.get('name')
    user_list = read_users()

    with open("./data/users.json", 'w') as users_file:
        # Add user to list
        user_list.append(name)

        # Save list back to JSON
        json.dump({"users": user_list}, users_file)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
