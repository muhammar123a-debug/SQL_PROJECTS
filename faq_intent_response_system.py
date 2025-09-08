import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$"
)
cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS chatbot_db")
cursor.execute("CREATE DATABASE chatbot_db")
cursor.execute("USE chatbot_db")

cursor.execute("""
CREATE TABLE Users(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE Intents(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL UNIQUE,
description TEXT NULL
)
""")

cursor.execute("""
CREATE TABLE Messages(
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
message TEXT NOT NULL,
intent_id INT,
timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES Users(id),
FOREIGN KEY (intent_id) REFERENCES Intents(id)
)
""")

cursor.execute("""
CREATE TABLE Responses(
id INT AUTO_INCREMENT PRIMARY KEY,
intent_id INT,
response_text TEXT NOT NULL,
FOREIGN KEY (intent_id) REFERENCES Intents(id)
)
""")

print("INSERT OPERATION")
cursor.execute("""
INSERT INTO Users (username, email) VALUES ('Asim','asim@gmail.com'),('Zain','zain@gmail.com'),('Ammar','ammar@gmail.com')
""")
cursor.execute("""
SELECT * FROM Users
""")
for i in cursor.fetchall():
    print(i)

print("\n UPDATE OPERATION")
cursor.execute("""
UPDATE Users SET username="Ammar Khan" WHERE id=3
""")
cursor.execute("""
SELECT * FROM Users
""")
for i in cursor.fetchall():
    print(i)

print("\n DELETE OPERATION")
cursor.execute("""
DELETE FROM Users WHERE id = 2
""")
cursor.execute("""
SELECT * FROM Users
""")
for i in cursor.fetchall():
    print(i)

cursor.execute("""
INSERT INTO Intents (name, description) VALUES ('password_reset', 'User asking about password reset')
""")

cursor.execute("""
INSERT INTO Messages (user_id, message, intent_id) VALUES (1, 'Hello, how can I reset my password?', 1)
""")

# Update message text
cursor.execute("""
UPDATE Messages 
SET message = %s 
WHERE id = %s
""", ("Hello, I just joined the chatbot!", 1))

cursor.execute("""
SELECT * FROM Messages
""")
for i in cursor.fetchall():
    print(i)

cursor.execute("""
SELECT * FROM Intents
""")
for i in cursor.fetchall():
    print(i)

cursor.execute("""
SELECT * FROM Responses
""")
for i in cursor.fetchall():
    print(i)

conn.commit()
cursor.close()
conn.close()
