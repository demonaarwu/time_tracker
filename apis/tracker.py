import sqlite3

def is_tracker_exist(user_id: str) -> bool:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    search_sql = ''' SELECT unix_time FROM trackers WHERE user_id = ?'''
    search_result = cursor.execute(search_sql, [user_id]).fetchall()

    db.close()

    if len(search_result) >= 1:
        return True
    else:
        return False

def create_tracker(user_id: str, label_name: str, unix_time: int) -> None:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    create_sql = ''' INSERT INTO trackers (user_id, label_name, unix_time) VALUES(?, ?, ?)'''
    cursor.execute(create_sql, [user_id, label_name, unix_time])

    db.commit()
    db.close()

def delete_tracker(user_id: str) -> None:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    cursor.execute('DELETE FROM trackers WHERE user_id = ?', [user_id])

    db.commit()
    db.close()

def get_tracker(user_id: str):
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    tracker = {}
    search_result = cursor.execute('SELECT user_id, label_name, unix_time FROM trackers WHERE user_id = ?', [user_id]).fetchall()

    tracker["user_id"] = search_result[0][0]
    tracker["label_name"] = search_result[0][1]
    tracker["unix_time"] = search_result[0][2]

    return tracker

