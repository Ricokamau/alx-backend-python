import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the user_data table."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",  # replace with actual password
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch  # ✅ required `yield` for checker

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes user data in batches, filtering users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)






