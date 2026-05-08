def analyze_text(text):
    if not isinstance(text, str):
        return None

    stripped = text.strip()

    if not stripped:
        return {"characters": 0, "words": 0, "sentences": 0}

    characters = len(stripped)
    words = len(stripped.split())
    sentences = sum(1 for char in stripped if char in '.!?')

    return {"characters": characters, "words": words, "sentences": sentences}
