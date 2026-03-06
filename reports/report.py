import sqlite3

def generate_report():

    conn = sqlite3.connect("reviews.db")
    cursor = conn.cursor()

    cursor.execute("SELECT sentiment, COUNT(*) FROM reviews GROUP BY sentiment")
    sentiment_data = cursor.fetchall()

    cursor.execute("SELECT theme, COUNT(*) FROM reviews GROUP BY theme")
    theme_data = cursor.fetchall()

    report = "# Voice of Customer Report\n\n"

    report += "## Sentiment Summary\n"

    for s in sentiment_data:
        report += f"{s[0]} : {s[1]}\n"

    report += "\n## Theme Summary\n"

    for t in theme_data:
        report += f"{t[0]} : {t[1]}\n"

    report += """

## Action Items

### Product Team
Improve battery performance based on negative reviews.

### Marketing Team
Highlight sound quality as customers love it.

### Support Team
Prepare troubleshooting guides for battery issues.
"""

    with open("reports/global_report.md","w") as f:
        f.write(report)

    print("Report Generated")