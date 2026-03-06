def detect_theme(text):

    text = text.lower()

    if "battery" in text:
        return "Battery"

    if "sound" in text:
        return "Sound Quality"

    if "comfort" in text:
        return "Comfort"

    if "price" in text:
        return "Price"

    if "delivery" in text:
        return "Delivery"

    if "anc" in text:
        return "ANC"

    if "build" in text:
        return "Build Quality"

    return "General"