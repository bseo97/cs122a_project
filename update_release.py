from db_connector import db_connection
import mysql.connector
def update_release(rid:int, title:str):

    conn = db_connection()
    cursor = conn.cursor()

    query = f"""UPDATE releases SET title='{title}' WHERE rid = {rid}"""

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        return False

    conn.commit()
    cursor.close()
    conn.close()
    return True