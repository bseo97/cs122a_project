import datetime
import mysql.connector
from db_connector import db_connection

def insert_viewer(uid:int, email:str, nickname:str, street:str, city:str, state:str, zip:str, genres:str, joined_date:datetime.date, first:str, last:str, subscription:str):
    conn = db_connection()
    cursor = conn.cursor()
    #Query statement for insert into user and insert into viewer tables
    insert_into_user_table = f"INSERT INTO users(uid, email, joined_date, nickname, street, city, state, zip, genres)" \
    f"VALUES({uid},'{email}','{joined_date}','{nickname}','{street}','{city}','{state}','{zip}','{genres}')"
    insert_into_viewer_table = f"INSERT INTO viewers(uid, subscription, first_name, last_name)" \
    f"VALUES({uid},'{subscription}','{first}','{last}')"

    #Execute inserting into user first since it viewer relies on the foriegn key restraint from users
    try:
        cursor.execute(insert_into_user_table)
        cursor.execute(insert_into_viewer_table)
    except mysql.connector.Error as err:
        print("FAILED TO EXECUTE INSERT VIEWER QUERIES")
        print(err)
        return False

    conn.commit()
    cursor.close()
    conn.close()
    return True
