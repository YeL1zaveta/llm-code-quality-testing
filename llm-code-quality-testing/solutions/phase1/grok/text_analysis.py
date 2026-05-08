def analyze_text(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    # Handle empty or whitespace-only text
    if not text or text.strip() == "":
        return {"characters": 0, "words": 0, "sentences": 0}

    # Number of characters (including spaces)
    characters = len(text)

    # Number of words (ignore extra spaces)
    words = len(text.split())

    # Number of sentences
    sentences = 0
    for char in text:
        if char in ".!?":
            sentences += 1

    return {
        "characters": characters,
        "words": words,
        "sentences": sentences
    }
