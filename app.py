from flask import Flask, redirect, render_template, request, session, jsonify
from apis.helpers import login_required
from apis.label import get_labels, add_label, is_label_exist, delete_label
from apis.user import is_username_exist, check_password, add_user, get_user_id
from apis.history import create_history, get_todays_record, get_last_weeks_record, get_overall_record
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/add/<name>")
@login_required
def create_label(name):
    add_label(user_id=session["user_id"], label_name=name)
    return redirect("/")

@app.route("/login", methods=["POST", "GET"])
def login():
    # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        if not (username and password):
            return 'Please input username and password'
        elif not is_username_exist(username):
            return 'Username doesn\'t exist!'
        elif not check_password(username, password):
            return 'Invalid password'
        else:
            session["user_id"] = get_user_id(username)
            session["label_name"] = ''

            return redirect("/")

@app.route("/register", methods=["POST", "GET"])
def register():
    # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        if not (username and password):
            return 'Please input username and password'
        elif is_username_exist(username):
            return 'Username already exists!'
        else:
            add_user(username, password)
            return redirect("/")

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")


@app.route("/labels", methods=["GET", "POST"])
@login_required
def labels():
    if request.method == "POST":
        label_name = request.get_json()["label_name"]
        if not is_label_exist(label_name=label_name, user_id=session["user_id"]) and label_name != '':
            add_label(label_name=label_name, user_id=session["user_id"])

        return redirect("/")
    else:
        return jsonify(get_labels(user_id=session["user_id"]))

@app.route("/labels/l", methods=["POST"])
@login_required
def delete():
    label_name = request.get_json()["label_name"]
    
    if is_label_exist(label_name=label_name, user_id=session["user_id"]):
        delete_label(label_name=label_name, user_id=session["user_id"])
    
    return redirect("/")

@app.route("/history", methods=["POST"])
@login_required
def history():
    label_name = request.get_json()["label_name"]
    time = request.get_json()["time"]

    create_history(label_name=label_name, time=time, user_id=session["user_id"])

    session["label_name"] = ''

    return redirect("/")

@app.route("/time_tracker", methods=["POST", "GET"])
@login_required
def check_tracker():
    if request.method == 'GET':
        if session["label_name"] != '':
            return jsonify({"status": "true",  "label_name": session["label_name"], "unix_time": session["unix_time"]})
        else:
            return jsonify({"status": "false"})
    else:
        json = request.get_json()

        session["label_name"] = json["label_name"]
        session["unix_time"] = json["unix_time"]

        return redirect("/")
@app.route("/stats", methods=["GET"])
def stats():
    return render_template("stats.html")

@app.route("/records", methods=["GET"])
def records():
    records = {"todays_record": get_todays_record(session["user_id"]),
               "last_weeks_record": get_last_weeks_record(session["user_id"]),
               "overall_record": get_overall_record(session["user_id"])}
    return jsonify(records)
