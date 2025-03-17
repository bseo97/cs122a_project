from db_connector import db_connection
import mysql.connector

def videos_viewed(rid:int):
    conn = db_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT Videos.rid, Videos.ep_num, Videos.title, Videos.length, COUNT(DISTINCT Sessions.uid) AS view_count
    FROM Videos
    LEFT JOIN Sessions ON Videos.rid = Sessions.rid AND Videos.ep_num = Sessions.ep_num
    WHERE Videos.rid = {rid}
    GROUP BY Videos.rid, Videos.ep_num, Videos.title, Videos.length
    ORDER BY Videos.rid DESC;
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