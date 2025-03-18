from db_connector import db_connection
import mysql.connector

def videos_viewed(rid:int):
    conn = db_connection()
    cursor = conn.cursor()


    cursor.execute("USE cs122a;")

    query = f"""
    SELECT videos.rid, videos.ep_num, videos.title, videos.length, COUNT(DISTINCT sessions.uid) AS view_count
    FROM videos
    LEFT JOIN sessions ON videos.rid = sessions.rid AND videos.ep_num = sessions.ep_num
    WHERE videos.rid = {rid}
    GROUP BY videos.rid, videos.ep_num, videos.title, videos.length
    ORDER BY videos.rid DESC;
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