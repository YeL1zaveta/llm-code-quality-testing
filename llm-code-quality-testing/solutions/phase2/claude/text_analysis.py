import re

def analyze_text(text):
    if not isinstance(text, str):
        return False

    characters = len(text)

    words = len(text.split()) if text.strip() else 0

    sentences = len(re.findall(r'[.!?]+', text))

    return {"characters": characters, "words": words, "sentences": sentences}