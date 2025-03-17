from db_connector import db_connection
import mysql.connector
def delete_viewer(uid:int):
    
    conn = db_connection()
    cursor = conn.cursor()

    #Delete query
    delete_query = f"DELETE FROM users WHERE users.uid = {uid}"

    try:
        cursor.execute(delete_query)
    except mysql.connector.Error as err:
        print("Error in delete viewer")
        return False

    conn.commit()
    cursor.close()
    conn.close()
    return True


