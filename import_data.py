import mysql.connector
import os
import csv
from db_connector import db_connection  # Import the function
from create_tables import create_tables

def import_csv_data(fileName):
    """Loads CSV files into MySQL tables using Python."""
    try:
        
        conn = db_connection()  # Use the imported function
        cursor = conn.cursor()

        test_data_folder = os.path.abspath(fileName)  # Ensure it's absolute
        #print(f"Using test data folder: {test_data_folder}")  # Debugging

        # dict of CSV files and corresponding tables
        csv_files = {
            "users.csv": "users",
            "producers.csv": "producers",
            "viewers.csv": "viewers",
            "releases.csv": "releases",
            "movies.csv": "movies",
            "series.csv": "series",
            "videos.csv": "videos",
            "sessions.csv": "sessions",
            "reviews.csv": "reviews"
        }

        load_query = {
                "users.csv":
                """
                INSERT INTO users(uid, email, joined_date, nickname, street, city, state, zip, genres)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                "producers.csv":
                """
                INSERT INTO producers(uid,bio,company)
                VALUES(%s, %s, %s) 
                """,
                "viewers.csv":
                """
                INSERT INTO viewers(uid,subscription,first_name,last_name)
                VALUES(%s, %s, %s, %s) 
                """,
                "releases.csv":
                """
                INSERT INTO releases(rid,producer_uid,title,genre,release_date)
                VALUES(%s, %s, %s, %s, %s) 
                """,
                "movies.csv": 
                """
                INSERT INTO movies(rid,website_url)
                VALUES(%s,%s)
                """,
                "series.csv":
                """
                INSERT INTO series(rid,introduction)
                VALUES(%s,%s)
                """,
                "videos.csv":
                """
                INSERT INTO videos(rid,ep_num,title,length)
                VALUES (%s,%s,%s,%s)
                """,
                "sessions.csv":
                """
                INSERT INTO sessions(sid,uid,rid,ep_num,initiate_at,leave_at,quality,device)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                """,
                "reviews.csv":
                """
                INSERT INTO reviews(rvid,uid,rid,rating,body,posted_at)
                VALUES(%s,%s,%s,%s,%s,%s)
                """
            }

        for file, table in csv_files.items():
            #print(file, table)
            file_path = os.path.join(test_data_folder, file)       # to find all CSV files within main directory
            csv_path = os.path.abspath(file_path).replace("\\", "/")    #to correctly read test_data folder (python originally interprets \t as tab)
            cursor.execute("SET foreign_key_checks=0") #Set key restraint to zero so that tables with key restraints can be deleted
            cursor.execute(f"TRUNCATE TABLE {table};")  # Delete existing records
            #print(f"Loading: {csv_path}")

            # load_query = f"""
            #     LOAD DATA LOCAL INFILE '{csv_path}'
            #     INTO TABLE {table}
            #     FIELDS TERMINATED BY ',' 
            #     LINES TERMINATED BY '\\n' 
            #     IGNORE 1 ROWS;
            # """

            try:
                with open(csv_path, 'r') as csvFile:
                    reader = csv.reader(csvFile)
                    next(reader) #Skips the header which is typically a list of parameter values for the table. 
                    for row in reader:
                        cursor.execute(load_query[file], row)
                #print(f"Loaded {file} into {table}")
            except mysql.connector.Error as err:
                print(f"Error loading {file}: {err}")
            
            cursor.execute("SET foreign_key_checks=1")# Put back on key restraints
        conn.commit()
        #print("all CSV files imported successfully")

    except mysql.connector.Error as err:
        #print(f"Database error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()
        return True
