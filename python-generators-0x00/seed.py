import mysql.connector
import csv
import uuid

# Connect to MySQL server (not a specific DB yet)
def connect_db():
    return mysql.connector.connect(
        user='root', password='your_password', host='localhost'
    )

# Create the database ALX_prodev
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

# Connect to the ALX_prodev DB
def connect_to_prodev():
    return mysql.connector.connect(
        user='root', password='your_password', host='localhost', database='ALX_prodev'
    )

# Create user_data table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL
        )
    ''')
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()

# Insert data from CSV
def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            ''', (str(uuid.uuid4()), row['name'], row['email'], row['age']))
    connection.commit()
    cursor.close()
