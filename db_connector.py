import mysql.connector
import os

# Replace these with your MySQL credentials
def db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database="cs122a",
        allow_local_infile=True      # loading local files
    )

    cursor = conn.cursor()

    try:
        # Attempt to enable local_infile globally (requires SUPER privilege)
        cursor.execute("SET GLOBAL local_infile = 1;")
        print("Enabled local_infile globally.")
    except mysql.connector.Error as err:
        print(f"Could not enable local_infile globally: {err}")

    cursor.close()
    return conn  # Return connection with local_infile enabled
