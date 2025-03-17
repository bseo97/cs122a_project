from db_connector import db_connection
import mysql.connector

def get_releases(uid:int):
    conn = db_connection()
    cursor = conn.cursor()

    #Get rid,genre,title from the natural joined table of reviews,viewers,releases where uid is equal to the passed in uid. Order it by ascending order based on title
    query = f"""SELECT DISTINCT rid, genre, title FROM reviews NATURAL JOIN viewers NATURAL JOIN releases WHERE uid = {uid} ORDER BY title ASC"""

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print(err)

    #Get the return value of the query
    queryValue = cursor.fetchall()

    cursor.close()
    conn.close()
    return queryValue