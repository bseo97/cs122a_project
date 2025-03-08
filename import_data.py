import mysql.connector
import os
from db_connector import db_connection  # Import the function
from create_tables import create_tables

def import_csv_data(fileName):
    """Loads CSV files into MySQL tables using Python."""
    try:
        
        conn = db_connection()  # Use the imported function
        cursor = conn.cursor()

        test_data_folder = os.path.abspath(fileName)  # Ensure it's absolute
        print(f"Using test data folder: {test_data_folder}")  # Debugging

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

        for file, table in csv_files.items():
            file_path = os.path.join(test_data_folder, file)       # to find all CSV files within main directory
            csv_path = os.path.abspath(file_path).replace("\\", "/")    #to correctly read test_data folder (python originally interprets \t as tab)

            cursor.execute("SET foreign_key_checks=0") #Set key restraint to zero so that tables with key restraints can be deleted
            cursor.execute(f"TRUNCATE TABLE {table};")  # Delete existing records
            cursor.execute("SET foreign_key_checks=1")# Put back on key restraints

            print(f"Loading: {csv_path}")

            load_query = f"""
                LOAD DATA LOCAL INFILE '{csv_path}'
                INTO TABLE {table}
                FIELDS TERMINATED BY ',' 
                LINES TERMINATED BY '\\n' 
                IGNORE 1 ROWS;
            """
            try:
                cursor.execute(load_query)
                print(f"Loaded {file} into {table}")
            except mysql.connector.Error as err:
                print(f"Error loading {file}: {err}")

        conn.commit()
        print("all CSV files imported successfully")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()
        return True
