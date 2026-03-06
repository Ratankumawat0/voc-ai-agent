def get_sentiment(text):

    text = text.lower()

    positive = [
        "good","great","excellent","amazing",
        "best","love","perfect","awesome"
    ]

    negative = [
        "bad","poor","worst","terrible",
        "hate","problem","issue"
    ]

    for p in positive:
        if p in text:
            return "Positive"

    for n in negative:
        if n in text:
            return "Negative"

    return "Neutral"