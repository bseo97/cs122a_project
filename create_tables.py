import mysql.connector
from db_connector import db_connection


def create_tables(): 
    conn = db_connection()  # Use the imported function
    cursor = conn.cursor()

    cursor.execute("USE cs122a;")   # Assumed that we already have cs122a database

    create_table_queries = {
        "users": """
                CREATE TABLE IF NOT EXISTS users (
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
        "producers": """
                CREATE TABLE IF NOT EXISTS producers (
                    uid INT,
                    bio TEXT,
                    company TEXT,
                    PRIMARY KEY (uid),
                    FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE
                );
            """,
        "viewers": """
                CREATE TABLE IF NOT EXISTS viewers (
                    uid INT,
                    subscription ENUM('free', 'monthly', 'yearly'),
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    PRIMARY KEY (uid),
                    FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE
                );
            """,
        "releases": """
                CREATE TABLE IF NOT EXISTS releases (
                    rid INT,
                    producer_uid INT NOT NULL,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    release_date DATE NOT NULL,
                    PRIMARY KEY (rid),
                    FOREIGN KEY (producer_uid) REFERENCES producers(uid) ON DELETE CASCADE
                );
            """,
        "movies": """
                CREATE TABLE IF NOT EXISTS movies (
                    rid INT,
                    website_url TEXT,
                    PRIMARY KEY (rid),
                    FOREIGN KEY (rid) REFERENCES releases(rid) ON DELETE CASCADE
                );
            """,
        "series": """
                CREATE TABLE IF NOT EXISTS series (
                    rid INT,
                    introduction TEXT,
                    PRIMARY KEY (rid),
                    FOREIGN KEY (rid) REFERENCES releases(rid) ON DELETE CASCADE
                );
            """,
        "videos": """
                CREATE TABLE IF NOT EXISTS videos (
                    rid INT,
                    ep_num INT NOT NULL,
                    title TEXT NOT NULL,
                    length INT NOT NULL,
                    PRIMARY KEY (rid, ep_num),
                    FOREIGN KEY (rid) REFERENCES releases(rid) ON DELETE CASCADE
                );
            """,
        "sessions": """
                CREATE TABLE IF NOT EXISTS sessions (
                    sid INT,
                    uid INT NOT NULL,
                    rid INT NOT NULL,
                    ep_num INT NOT NULL,
                    initiate_at DATETIME NOT NULL,
                    leave_at DATETIME NOT NULL,
                    quality ENUM('480p', '720p', '1080p'),
                    device ENUM('mobile', 'desktop'),
                    PRIMARY KEY (sid),
                    FOREIGN KEY (uid) REFERENCES viewers(uid) ON DELETE CASCADE,
                    FOREIGN KEY (rid, ep_num) REFERENCES videos(rid, ep_num) ON DELETE CASCADE
                );
            """,
        "reviews": """
                CREATE TABLE IF NOT EXISTS reviews (
                    rvid INT,
                    uid INT NOT NULL,
                    rid INT NOT NULL,
                    rating DECIMAL(2, 1) NOT NULL CHECK (rating BETWEEN 0 AND 5),
                    body TEXT,
                    posted_at DATETIME NOT NULL,
                    PRIMARY KEY (rvid),
                    FOREIGN KEY (uid) REFERENCES viewers(uid) ON DELETE CASCADE,
                    FOREIGN KEY (rid) REFERENCES releases(rid) ON DELETE CASCADE
                );
            """
    }

    for table, query in create_table_queries.items():
        try:
            cursor.execute(query)
            #print(f"Created table: {table}")
        except mysql.connector.Error as err:
            print(f"Error creating table {table}: {err}")

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
    #print("All tables created")



