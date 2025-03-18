from db_connector import db_connection
import mysql.connector

def popular_release(N:int):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("USE cs122a;")
    query = """
    SELECT releases.rid, releases.title, COUNT(reviews.rid) AS reviewCount
    FROM releases
    JOIN reviews ON releases.rid = reviews.rid
    GROUP BY releases.rid, releases.title
    ORDER BY reviewCount DESC, releases.rid DESC
    LIMIT %s
    """


    try:
        cursor.execute(query, (N,))
    except mysql.connector.Error as err:
        print(err)

    #Get the return value of the query
    queryValue = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryValue