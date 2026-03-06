import sqlite3

DB_NAME = "reviews.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT,
        rating INTEGER,
        title TEXT,
        review TEXT UNIQUE,
        sentiment TEXT,
        theme TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_review(product, rating, title, review, sentiment, theme, date):

    conn = connect()
    cur = conn.cursor()

    try:

        cur.execute("""
        INSERT INTO reviews(product,rating,title,review,sentiment,theme,date)
        VALUES(?,?,?,?,?,?,?)
        """,(product,rating,title,review,sentiment,theme,date))

        conn.commit()

    except:
        pass

    conn.close()