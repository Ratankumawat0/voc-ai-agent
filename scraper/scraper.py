from analysis.sentiment import get_sentiment
from analysis.themes import detect_theme
from database.db import insert_review
from datetime import date

def scrape_reviews():

    print("Fetching Reviews...")

    reviews = [

        {
            "product":"Master Buds 1",
            "rating":5,
            "title":"Amazing sound",
            "review":"Amazing sound quality and good battery life"
        },

        {
            "product":"Master Buds Max",
            "rating":2,
            "title":"Poor battery",
            "review":"Battery life is poor and sound is bad"
        },

        {
            "product":"Master Buds 1",
            "rating":4,
            "title":"Comfortable",
            "review":"Very comfortable earbuds with great sound"
        },

        {
            "product":"Master Buds Max",
            "rating":3,
            "title":"Average product",
            "review":"Sound quality is good but battery issue"
        }

    ]

    today = str(date.today())

    for r in reviews:

        sentiment = get_sentiment(r["review"])
        theme = detect_theme(r["review"])

        insert_review(
            r["product"],
            r["rating"],
            r["title"],
            r["review"],
            sentiment,
            theme,
            today
        )

    print("Reviews stored successfully")