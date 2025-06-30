from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the DB."""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    # Count total rows to calculate batch offsets
    cursor.execute("SELECT COUNT(*) AS total FROM user_data")
    total = cursor.fetchone()['total']

    for offset in range(0, total, batch_size):
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        yield rows  # ✅ Must use `yield`

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes users in batches, filters by age > 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)

