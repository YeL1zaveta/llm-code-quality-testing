import re

def analyze_text(text):
    if not isinstance(text, str):
        return False

    if not text:
        return {"characters": 0, "words": 0, "sentences": 0}

    # Character count includes everything
    char_count = len(text)

    # Word count: Split by whitespace and filter out empty strings
    words = text.split()
    word_count = len(words)

    # Sentence count: Use regex to find sequences of one or more ending punctuation marks
    # This treats "!!!" or "?." as a single sentence boundary
    sentences = re.findall(r'[.!?]+', text)
    sentence_count = len(sentences)

    return {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count
    }