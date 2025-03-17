from db_connector import db_connection
import mysql.connector

def insert_movie(rid:int, website_url:str):
    
    conn = db_connection()
    cursor = conn.cursor()

    #Insert into movies rid and website_url with argument values. Check if it is a duplicate, if it is replace website_url
    query = f"INSERT INTO movies(rid, website_url) VALUES ({rid}, '{website_url}') ON DUPLICATE KEY UPDATE website_url = '{website_url}'"

    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Insert Movie Failed: ",err )
        return False
    conn.commit()
    cursor.close()
    conn.close()
    return True
