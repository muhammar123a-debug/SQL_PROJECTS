import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$"
)
cursor = connect.cursor()

cursor.execute("DROP DATABASE IF EXISTS chatbot_db")
cursor.execute("CREATE DATABASE IF NOT EXISTS chatbot_db")
cursor.execute("USE chatbot_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) NOT NULL UNIQUE,
email VARCHAR(100) NULL UNIQUE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Conversations(
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ended_at TIMESTAMP NULL,
FOREIGN KEY (user_id) REFERENCES Users(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Messages(
id INT AUTO_INCREMENT PRIMARY KEY,
conversation_id INT,
sender ENUM('user', 'bot') NOT NULL,
message TEXT NOT NULL,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (conversation_id) REFERENCES Conversations(id)
)
""")

cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", ('ammar', 'ammar@gmail.com'))
cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", ('qasim', 'qasim@gmail.com'))
cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", ('sultan', 'sultan@gmail.com'))
cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", ('zubair', 'zubair@gmail.com'))
cursor.execute("INSERT INTO Users (username, email) VALUES (%s, %s)", ('sufiyan', 'sufiyan@gmail.com'))

cursor.execute("INSERT INTO Conversations (user_id) VALUES (1)")
cursor.execute("INSERT INTO Conversations (user_id) VALUES (2)")
cursor.execute("INSERT INTO Conversations (user_id) VALUES (3)")
cursor.execute("INSERT INTO Conversations (user_id) VALUES (4)")
cursor.execute("INSERT INTO Conversations (user_id) VALUES (5)")

cursor.execute("INSERT INTO Messages(conversation_id, sender, message) VALUES (%s, %s, %s)",(1, 'user', 'Hello there!'),(1, 'bot', 'Hello Ammar! How can I help you today?'))
cursor.execute("INSERT INTO Messages(conversation_id, sender, message) VALUES (%s, %s, %s)",(2, 'user', 'Hello there!'),(2, 'bot', 'Hello Anas! How can I help you today?'))
cursor.execute("INSERT INTO Messages(conversation_id, sender, message) VALUES (%s, %s, %s)",(3, 'user', 'Hello there!'),(3, 'bot', 'Hello Qasim! How can I help you today?'))
cursor.execute("INSERT INTO Messages(conversation_id, sender, message) VALUES (%s, %s, %s)",(4, 'user', 'Hello there!'),(4, 'bot', 'Hello Furqan! How can I help you today?'))
cursor.execute("INSERT INTO Messages(conversation_id, sender, message) VALUES (%s, %s, %s)",(5, 'user', 'Hello there!'),(5, 'bot', 'Hello Yanis! How can I help you today?'))
cursor.execute("SELECT * FROM Users")
for i in cursor.fetchall():
    print(i)
cursor.execute("SELECT * FROM Conversations")
for i in cursor.fetchall():
    print(i)
cursor.execute("SELECT * FROM Messages")
for i in cursor.fetchall():
    print(i)
connect.commit()

print("Users table created successfully.")