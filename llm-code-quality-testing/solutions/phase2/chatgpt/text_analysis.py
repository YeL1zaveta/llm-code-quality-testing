import re

def analyze_text(text):
    if not isinstance(text, str):
        return False

    if text == "":
        return {"characters": 0, "words": 0, "sentences": 0}

    characters = len(text)

    words = len([w for w in text.split() if w])

    sentence_groups = re.findall(r'[.!?]+', text)
    sentences = len(sentence_groups) if sentence_groups else 0

    return {
        "characters": characters,
        "words": words,
        "sentences": sentences
    }