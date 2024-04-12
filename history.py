import sqlite3
import datetime

def create_history(label_name: str, time: str, user_id: str):
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    date = datetime.date.today()

    cursor.execute("INSERT INTO history (user_id, label_name, time, date) VALUES (?, ?, ?, ?)", 
                   [user_id, label_name, time, date])

    db.commit()
    db.close()

def get_todays_record(user_id: str) -> dict:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()
    date = datetime.date.today()

    records = cursor.execute("SELECT label_name, time FROM history WHERE user_id = ? and date = ?", [user_id, date]).fetchall()
    db.close()

    todays_record = {}
    for record in records:
        label_name = record[0]
        time = record[1]
        if label_name in todays_record.keys():
            todays_record[label_name] += time
        else:
            todays_record[label_name] = time

    return todays_record

def get_last_weeks_record(user_id: str) -> dict:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()
    date = datetime.date.today() - datetime.timedelta(days=7)

    records = cursor.execute("SELECT label_name, time FROM history WHERE user_id = ? and date > ?", [user_id, date]).fetchall()
    db.close()

    last_weeks_record = {}
    for record in records:
        label_name = record[0]
        time = record[1]

        if label_name in last_weeks_record.keys():
            last_weeks_record[label_name] += time
        else:
            last_weeks_record[label_name] = time

    return last_weeks_record

def get_overall_record(user_id: str) -> dict:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    records = cursor.execute("SELECT label_name, time FROM history WHERE user_id = ?", [user_id]).fetchall()

    overall_record = {}
    for record in records:
        label_name = record[0]
        time = record[1]

        if label_name in overall_record.keys():
            overall_record[label_name] += time
        else:
            overall_record[label_name] = time

    return overall_record
