def analyze_text(text):
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        # Normalize text by stripping extra spaces
        cleaned_text = text.strip()

        if not cleaned_text:
            return {"characters": 0, "words": 0, "sentences": 0}

        # Character count (excluding leading/trailing spaces only)
        char_count = len(cleaned_text)

        # Word count (split by whitespace, ignore extra spaces)
        words = cleaned_text.split()
        word_count = len(words)

        # Sentence count (based on ., !, ?)
        sentence_count = 0
        in_sentence = False
        for ch in cleaned_text:
            if ch not in ".!?":
                in_sentence = True
            elif in_sentence:
                sentence_count += 1
                in_sentence = False

        return {
            "characters": char_count,
            "words": word_count,
            "sentences": sentence_count
        }

    except Exception:
        return None