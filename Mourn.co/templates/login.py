import sqlite3  # Import the sqlite3 module to work with SQLite databases
import hashlib  # Import the hashlib module for hashing passwords
# Connect to the SQLite database 'userdata.db' (creates it if it doesn't exist)
conn = sqlite3.connect('userdata.db')
# Create a cursor object to interact with the database
cur = conn.cursor()
# Execute a SQL command to create the 'userdata' table if it doesn't already exist
cur.execute("""CREATE TABLE IF NOT EXISTS userdata(
            Id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
            )""")

# Define usernames and their respective hashed passwords
username1, password1 = "Streetysteals", hashlib.sha256("Gotsthemdeals".encode()).hexdigest()
username2, password2 = "Bussylusy", hashlib.sha256("Eatsthatpssy".encode()).hexdigest()
username3, password3 = "Bluecheese", hashlib.sha256("Moldyinfection".encode()).hexdigest()
username4, password4 = "Cottagecheese", hashlib.sha256("Withspinagesalad".encode()).hexdigest()
username5, password5 = "Obesity", hashlib.sha256("Asmrgluttony".encode()).hexdigest()

# Insert the user data into the 'userdata' table
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))
conn.commit()