import sqlite3
from datetime import date

def generate_weekly_report():

    today = str(date.today())

    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM reviews WHERE date=?",(today,))

    rows = cur.fetchall()

    report = "# Weekly Delta Report\n\n"

    report += f"New Reviews Today : {len(rows)}\n\n"

    for r in rows:
        report += f"{r[1]} | {r[4]} | {r[5]}\n"

    with open("reports/weekly_report.md","w") as f:
        f.write(report)

    print("Weekly report generated")

    conn.close()