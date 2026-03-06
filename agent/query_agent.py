import sqlite3

def ask_agent(question):

    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()

    question = question.lower()

    if "battery" in question:

        cur.execute("SELECT COUNT(*) FROM reviews WHERE theme='Battery'")
        count = cur.fetchone()[0]

        print(f"Battery related complaints : {count}")

    elif "sound" in question:

        cur.execute("SELECT COUNT(*) FROM reviews WHERE theme='Sound Quality'")
        count = cur.fetchone()[0]

        print(f"Sound quality mentions : {count}")

    elif "comfort" in question:

        cur.execute("SELECT COUNT(*) FROM reviews WHERE theme='Comfort'")
        count = cur.fetchone()[0]

        print(f"Comfort mentions : {count}")

    else:

        print("Agent could not understand the question")

    conn.close()