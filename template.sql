CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  username TEXT NOT NULL,
  hash TEXT NOT NULL
);
CREATE TABLE labels(
  user_id INTEGER NOT NULL,
  label_name TEXT NOT NULL
);
CREATE TABLE history(
  user_id INTEGER NOT NULL,
  label_name TEXT NOT NULL,
  time INTEGER NOT NULL,
  date TEXT NOT NULL
);
CREATE TABLE trackers(
  user_id INTEGER NOT NULL,
  label_name TEXT NOT NULL,
  unix_time INTEGER NOT NULL,
);
