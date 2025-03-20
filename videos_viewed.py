from db_connector import db_connection
import mysql.connector

def videos_viewed(rid:int):
    conn = db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("USE cs122a;")

        count_query = """
        SELECT COUNT(DISTINCT uid)
        FROM sessions
        WHERE rid = %s
        """
    
        cursor.execute(count_query, (rid,))
        total_unique_viewers = cursor.fetchone()[0] or 0

        videos_query = """
        SELECT RID, ep_num, title, length
        FROM videos
        WHERE rid = %s
        """

        cursor.execute(videos_query, (rid,))
        videos = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(err)
        return ([], 0)
    finally:
        cursor.close()
        conn.close()
    
    return (videos, total_unique_viewers)