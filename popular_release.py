from db_connector import db_connection
import mysql.connector

def popular_release(N:int):
    conn = db_connection()
    cursor = conn.cursor()

    query = f"""
    SELECT rid, title, COUNT(rid) AS reviewCount
    FROM Reviews
    NATURAL JOIN Releases
    GROUP BY rid, title
    ORDER BY reviewCount DESC, rid ASC
    LIMIT {N}
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