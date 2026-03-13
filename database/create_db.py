import sqlite3

conn = sqlite3.connect("skill_platform.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
email TEXT,
phone TEXT,
education TEXT,
skill TEXT,
password TEXT
);
""")

cursor.execute("""
CREATE TABLE chats(
id INTEGER PRIMARY KEY AUTOINCREMENT,
sender TEXT,
receiver TEXT,
message TEXT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE skills(
id INTEGER PRIMARY KEY AUTOINCREMENT,
skill_name TEXT,
title TEXT,
link TEXT
);
""")

cursor.execute("""
CREATE TABLE connections(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user1 TEXT,
user2 TEXT,
status TEXT,
request_type TEXT         
);
""")

cursor.execute("""
CREATE TABLE notifications(
id INTEGER PRIMARY KEY AUTOINCREMENT,
receiver TEXT,
sender TEXT,
message TEXT,
status TEXT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()

print("Database created successfully")