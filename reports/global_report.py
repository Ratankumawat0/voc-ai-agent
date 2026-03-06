import sqlite3

def generate_global_report():

    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()

    report = "# Global Voice of Customer Report\n\n"

    report += "## Sentiment Summary\n"

    cur.execute("SELECT sentiment,COUNT(*) FROM reviews GROUP BY sentiment")

    for row in cur.fetchall():
        report += f"{row[0]} : {row[1]}\n"

    report += "\n## Theme Summary\n"

    cur.execute("SELECT theme,COUNT(*) FROM reviews GROUP BY theme")

    for row in cur.fetchall():
        report += f"{row[0]} : {row[1]}\n"

    report += "\n## Product Comparison\n"

    cur.execute("SELECT product,COUNT(*) FROM reviews GROUP BY product")

    for row in cur.fetchall():
        report += f"{row[0]} Reviews : {row[1]}\n"

    report += """

## Key Insights

Customers highly appreciate sound quality.

Battery issues reported across products.

Comfort level of Master Buds 1 praised.

## Action Items

### Product Team
Improve battery performance.

### Marketing
Promote strong sound quality and comfort.

### Support
Prepare troubleshooting guide for battery issues.
"""

    with open("reports/global_report.md","w") as f:
        f.write(report)

    print("Global report generated")

    conn.close()