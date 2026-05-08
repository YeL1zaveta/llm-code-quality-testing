def analyze_text(text):
    if not isinstance(text, str):
        return False
    if not text:
        return {"characters": 0, "words": 0, "sentences": 0}
    characters = len(text)
    words = len(text.split())
    sentences = 0
    prev_was_terminator = False
    terminators = {'.', '!', '?'}
    for char in text:
        if char in terminators:
            if not prev_was_terminator:
                sentences += 1
            prev_was_terminator = True
        else:
            prev_was_terminator = False
    return {
        "characters": characters,
        "words": words,
        "sentences": sentences
    }