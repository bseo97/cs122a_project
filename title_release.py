from db_connector import db_connection
import mysql.connector

def title_release(sid:int):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("USE cs122a;")

    query = """
    SELECT releases.rid, releases.title AS release_title, releases.genre, videos.title AS video_title, videos.ep_num, videos.length
    FROM sessions
    JOIN videos ON sessions.rid = videos.rid AND sessions.ep_num = videos.ep_num
    JOIN releases ON videos.rid = releases.rid
    WHERE sessions.sid = %s
    ORDER BY releases.title ASC;
    """

    try:
        cursor.execute(query, (sid,))
    except mysql.connector.Error as err:
        print(err)

    #Get the return value of the query
    queryValue = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryValue