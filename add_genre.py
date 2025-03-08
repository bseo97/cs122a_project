from db_connector import db_connection
import mysql.connector

def add_genre(uid:int, genre:str):

    conn = db_connection()
    cursor = conn.cursor()
    try:
        #Retrieve the value in genre table of user uid
        retreive_query = f"SELECT genres FROM users WHERE users.uid = {uid}"
        cursor.execute(retreive_query)
        retreive_value = cursor.fetchall()[0][0]
        print(retreive_value)

        #Append user input genre into genre string
        retreive_value = f"{genre};" + retreive_value

        #Update genre value in users with new genre string
        update_query = f"UPDATE users SET genres='{retreive_value}' WHERE users.uid = {uid}"
        cursor.execute(update_query)
    except mysql.connector.Error as err:
        print("Error with adding genre")
        return False

    conn.commit()
    cursor.close()
    conn.close()
    return True
