import sqlite3

URL = "dev.db"
conn = sqlite3.connect(URL)

conn.execute('''
CREATE TABLE IF NOT EXISTS level (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    sentence MEDIUMTEXT,
    difficulty INTEGER DEFAULT 1,
    score INTEGER DEFAULT 100
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS room (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    max INTEGER DEFAULT 2
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    current_room INTEGER DEFAULT NULL,
    FOREIGN KEY(current_room) REFERENCES room(id)
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS completed_levels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER,
    userId INTEGER NOT NULL,
    levelId INTEGER NOT NULL,
    FOREIGN KEY(userId) REFERENCES user(id),
    FOREIGN KEY(levelId) REFERENCES level(id)
)
''')

conn.commit()