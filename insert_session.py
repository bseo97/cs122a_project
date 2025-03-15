from db_connector import db_connection
import mysql.connector
import datetime

def insert_session(sid:int, uid:int, rid:int, ep_num:int, initiate_at:datetime, leave_at:datetime, quality:str, device:str):

    conn = db_connection()
    cursor = conn.cursor()
    
    #Query for inserting session
    query = f"""INSERT INTO sessions(sid, uid, rid, ep_num, initiate_at, leave_at, quality, device) 
    VALUES ('{sid}', '{uid}', '{rid}', {ep_num}, '{initiate_at}', '{leave_at}', '{quality}','{device}')
    """

    try:
        cursor.execute(query)

    except mysql.connector.Error as err:
        # print("Error in inserting session: ", err)
        return False

    conn.commit()
    cursor.close()
    conn.close()
    return True

