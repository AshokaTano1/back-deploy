from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
USERS = [
 {"id": 1, "name": "Ashley W. Walker", "phone": "317-769-0638", "birthday": "August 12, 1999", "email": "AshleyWWalker@dayrep.com", "username": "Joull1999"},
 {"id": 2, "name": "Martin M. Johnson", "phone": "301-962-1329", "birthday": "March 20, 1964", "email": "MartinMJohnson@teleworm.us", "username": "Youde1964"},
 {"id": 3, "name": "Justina D. Wallace", "phone": "914-819-0493", "birthday": "May 18, 1994", "email": "JustinaDWallace@rhyta.com", "username": "Donfe1994"},
 {"id": 4, "name": "Jason R. King", "phone": "608-562-1533", "birthday": "February 18, 1962", "email": "JasonRKing@dayrep.com", "username": "Ginusbact"},
 {"id": 5, "name": "Leroy T. Evans", "phone": "337-570-9574", "birthday": "January 7, 1946", "email": "LeroyTEvans@armyspy.com", "username": "Atiousaing"},
]
@app.route("/")
def hello_world():
 return "<p>Hello, World!</p>"

@app.route("/users-table", methods=["GET"])
def show_users():
    return render_template('users.html', users=USERS)

@app.route("/sum", methods=["POST"])
def square_number():
    input_number = int(request.form['number'])
    squared_number = input_number ** 2
    response = {'data': {'answer': squared_number}}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
