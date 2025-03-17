from db_connector import db_connection
import mysql.connector

def title_release(sid:int):
    conn = db_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT Releases.rid, Releases.title AS release_title, Releases.genre, Videos.title AS video_title, Videos.ep_num, Videos.length
    FROM Sessions
    JOIN Videos ON Sessions.rid = Videos.rid AND Sessions.ep_num = Videos.ep_num
    JOIN Releases ON Videos.rid = Releases.rid
    WHERE Sessions.sid = {sid}
    ORDER BY Releases.title ASC;
    """

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err)

    #Get the return value of the query
    queryValue = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryValue