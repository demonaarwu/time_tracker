import sqlite3

def get_labels(user_id: str) -> list:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    labels_data = [label[0] for label in cursor.execute("SELECT label_name FROM labels WHERE user_id = ?", [user_id]).fetchall()]
    db.close()
    return labels_data

def add_label(label_name: str, user_id: str) -> None:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    cursor.execute("INSERT INTO labels (label_name, user_id) VALUES (?, ?)",
                   [label_name, user_id])
    db.commit()
    db.close()

def delete_label(label_name: str, user_id: str) -> None:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    cursor.execute(
            "DELETE FROM labels WHERE label_name = ? and user_id = ?",
            [label_name, user_id]
            )

    cursor.execute(
            "DELETE FROM history WHERE label_name = ? and user_id = ?",
            [label_name, user_id]
            )
    db.commit()
    db.close()
   

def is_label_exist(label_name: str, user_id: str) -> bool:
    db = sqlite3.connect("./tracker.db", check_same_thread=False)
    cursor = db.cursor()

    search_result =cursor.execute("SELECT * FROM labels WHERE user_id = ? and label_name = ?",
                                  [user_id, label_name]).fetchall()
    db.close()

    if len(search_result) > 0:
        return True
    else:
        return False
