from db_connector import db_connection
import mysql.connector

def add_genre(uid:int, genre:str):

    conn = db_connection()
    cursor = conn.cursor()
    try:
        #Retrieve the value in genre table of user uid
        retreive_query = f"SELECT genres FROM users WHERE users.uid = {uid}"
        cursor.execute(retreive_query)
        retreive_value = cursor.fetchall()
        #If the same genre is in the string return false
        if genre in retreive_value[0][0].split(";"):
            return False
        retreive_value = retreive_value[0][0]

        #Append user input genre into genre string. If the string is empty then just add the genre into the string.
        if len(retreive_value) == 0:
            retreive_value = genre
        else:
            retreive_value = f"{retreive_value};" + genre

        #Update genre value in users with new genre string
        update_query = f"UPDATE users SET genres='{retreive_value}' WHERE users.uid = {uid}"
        cursor.execute(update_query)
    except mysql.connector.Error as err:
        print("Error with adding genre: " + err)
        return False

    conn.commit()
    cursor.close()
    conn.close()
    return True
