from db_connector import db_connection
import mysql.connector
import datetime

def active_viewers(N:int, start:datetime.date, end:datetime.date):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("USE cs122a;")

    query = f"""
    SELECT viewers.uid, viewers.first_name, viewers.last_name
    FROM sessions
    JOIN viewers ON sessions.uid = viewers.uid
    WHERE sessions.initiate_at BETWEEN %s AND %s
    GROUP BY viewers.uid, viewers.first_name, viewers.last_name
    HAVING COUNT(sessions.sid) >= %s
    ORDER BY viewers.uid ASC;
    """

    try:
        cursor.execute(query, (start, end, N))
    except mysql.connector.Error as err:
        print(err)

    #Get the return value of the query
    queryValue = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryValue