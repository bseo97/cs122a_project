from db_connector import db_connection
import mysql.connector
import datetime

def active_viewers(N:int, start:datetime.date, end:datetime.date):
    conn = db_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT Viewers.uid, Viewers.first, Viewers.last
    FROM Sessions
    JOIN Viewers ON Sessions.uid = Viewers.uid
    WHERE Sessions.initiate_at BETWEEN '{start}' AND '{end}'
    GROUP BY Viewers.uid, Viewers.first, Viewers.last
    HAVING COUNT(Sessions.sid) >= {N}
    ORDER BY Viewers.uid ASC;
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