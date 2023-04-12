from flask import Flask, render_template, request, redirect
import sqlite3
from flask_bcrypt import Bcrypt
from flask_socketio import join_room, leave_room, SocketIO, send, emit
from flask_login import LoginManager, login_user

URL = "dev.db"

app = Flask(__name__)
app.config["DEBUG"] = True
bcrypt = Bcrypt(app)
socketio = SocketIO(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(URL)
    query = conn.execute(f"SELECT * FROM user WHERE id=?", (user_id,))
    user = query.fetchone()
    return user

@app.route("/")
def index():
    conn = sqlite3.connect(URL)
    users = conn.execute("SELECT * FROM user").fetchall()
    return render_template("index.html", users=users)

@app.route("/api/users", methods=["GET", "POST"])
def Users():
    conn = sqlite3.connect(URL)
    if request.method == "POST":
        form = request.json
        name = form["name"]
        username = form["username"]
        password = bcrypt.generate_password_hash(form["password"], 10).decode("utf-8")
        conn.execute(f'INSERT INTO user (name, username, password) VALUES ("{name}", "{username}", "{password}")')
        conn.commit()
        return redirect("/")
    if request.method == "GET":
        users = conn.execute('SELECT * FROM user').fetchall()
        return users

@app.route("/api/users/<int:id>", methods=["DELETE", "GET"])
def UserInfo(id):
    conn = sqlite3.connect(URL)
    if request.method == "DELETE":
        conn.execute(f"DELETE FROM user WHERE id={id}")
        conn.commit()
        return redirect("/")
    return redirect("/")

@app.route("/login")
def LoginPage():
    return render_template("login.html")

@app.route("/api/users/login", methods=["POST"])
def Login():
    conn = sqlite3.connect(URL)
    if request.method == "POST":
        form = request.json
        username = form["username"]
        password = form["password"]
        selected_user = conn.execute(f"SELECT * FROM user WHERE username='{username}'").fetchone()
        if selected_user:
            if bcrypt.check_password_hash(selected_user[3], password):
                # return login_user(selected_user)
                return {'message': selected_user}
            else:
                return {'message': "error"}

        else:
            return {'message': "error"}
 
    return ''

@app.route("/api/level")
def GetLevel():
    conn = sqlite3.connect(URL)
    difficulty = request.args.get('difficulty', default=1, type=int)
    try:
        res = conn.execute(f"SELECT * FROM level WHERE difficulty='{difficulty}'").fetchall()
        return res
    except:
        return "Error"


@app.route("/rooms")
def JoinRooms():
    return render_template("join_room.html")

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send({"msg": username + " has joined the " + room}, room=room)
    print("JOINED!")

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send({"msg": username + " has left the " + room}, room=room)

@socketio.on("chat")
def on_chat(data):
    room = data['room']
    username = data['username']
    message = data['message']
    send({"msg": username + ": " + message}, room=room)

@socketio.on("ping")
def ping(data):
    print(data)

if __name__ == "__main__":
    socketio.run(app, port=8080)
