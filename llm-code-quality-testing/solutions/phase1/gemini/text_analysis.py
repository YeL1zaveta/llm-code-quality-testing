import re
def analyze_text(text):
    if not isinstance(text, str) or not text.strip():
        return {
            "characters": 0,
            "words": 0,
            "sentences": 0
        }

    # Character count including spaces
    char_count = len(text)

    # Word count: splitting by whitespace and filtering out empty strings
    words = text.split()
    word_count = len(words)

    # Sentence count: finding occurrences of '.', '!', or '?'
    # This handles multiple punctuation marks (e.g., "...") as one sentence break
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    sentence_count = len(sentences)

    # Fallback: if text has content but no punctuation, count as 1 sentence
    if sentence_count == 0 and word_count > 0:
        sentence_count = 1

    return {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count
    }