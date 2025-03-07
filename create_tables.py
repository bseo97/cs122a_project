import mysql.connector
from db_connector import db_connection


def create_tables(): 
    conn = db_connection()  # Use the imported function
    cursor = conn.cursor()

    cursor.execute("USE cs122a;")   # Assumed that we already have cs122a database

    create_table_queries = {
        "Users": """
                CREATE TABLE IF NOT EXISTS Users (
                    uid INT,
                    email TEXT NOT NULL,
                    joined_date DATE NOT NULL,
                    nickname TEXT NOT NULL,
                    street TEXT,
                    city TEXT,
                    state TEXT,
                    zip TEXT,
                    genres TEXT,
                    PRIMARY KEY (uid)
                );
            """,
        "Producers": """
                CREATE TABLE IF NOT EXISTS Producers (
                    uid INT,
                    bio TEXT,
                    company TEXT,
                    PRIMARY KEY (uid),
                    FOREIGN KEY (uid) REFERENCES Users(uid) ON DELETE CASCADE
                );
            """,
        "Viewers": """
                CREATE TABLE IF NOT EXISTS Viewers (
                    uid INT,
                    subscription ENUM('free', 'monthly', 'yearly'),
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    PRIMARY KEY (uid),
                    FOREIGN KEY (uid) REFERENCES Users(uid) ON DELETE CASCADE
                );
            """,
        "Releases": """
                CREATE TABLE IF NOT EXISTS Releases (
                    rid INT,
                    producer_uid INT NOT NULL,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    release_date DATE NOT NULL,
                    PRIMARY KEY (rid),
                    FOREIGN KEY (producer_uid) REFERENCES Producers(uid) ON DELETE CASCADE
                );
            """,
        "Movies": """
                CREATE TABLE IF NOT EXISTS Movies (
                    rid INT,
                    website_url TEXT,
                    PRIMARY KEY (rid),
                    FOREIGN KEY (rid) REFERENCES Releases(rid) ON DELETE CASCADE
                );
            """,
        "Series": """
                CREATE TABLE IF NOT EXISTS Series (
                    rid INT,
                    introduction TEXT,
                    PRIMARY KEY (rid),
                    FOREIGN KEY (rid) REFERENCES Releases(rid) ON DELETE CASCADE
                );
            """,
        "Videos": """
                CREATE TABLE IF NOT EXISTS Videos (
                    rid INT,
                    ep_num INT NOT NULL,
                    title TEXT NOT NULL,
                    length INT NOT NULL,
                    PRIMARY KEY (rid, ep_num),
                    FOREIGN KEY (rid) REFERENCES Releases(rid) ON DELETE CASCADE
                );
            """,
        "Sessions": """
                CREATE TABLE IF NOT EXISTS Sessions (
                    sid INT,
                    uid INT NOT NULL,
                    rid INT NOT NULL,
                    ep_num INT NOT NULL,
                    initiate_at DATETIME NOT NULL,
                    leave_at DATETIME NOT NULL,
                    quality ENUM('480p', '720p', '1080p'),
                    device ENUM('mobile', 'desktop'),
                    PRIMARY KEY (sid),
                    FOREIGN KEY (uid) REFERENCES Viewers(uid) ON DELETE CASCADE,
                    FOREIGN KEY (rid, ep_num) REFERENCES Videos(rid, ep_num) ON DELETE CASCADE
                );
            """,
        "Reviews": """
                CREATE TABLE IF NOT EXISTS Reviews (
                    rvid INT,
                    uid INT NOT NULL,
                    rid INT NOT NULL,
                    rating DECIMAL(2, 1) NOT NULL CHECK (rating BETWEEN 0 AND 5),
                    body TEXT,
                    posted_at DATETIME NOT NULL,
                    PRIMARY KEY (rvid),
                    FOREIGN KEY (uid) REFERENCES Viewers(uid) ON DELETE CASCADE,
                    FOREIGN KEY (rid) REFERENCES Releases(rid) ON DELETE CASCADE
                );
            """
    }

    for table, query in create_table_queries.items():
        try:
            cursor.execute(query)
            print(f"Created table: {table}")
        except mysql.connector.Error as err:
            print(f"Error creating table {table}: {err}")

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
    print("All tables created")



