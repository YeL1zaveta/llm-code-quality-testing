from solutions.phase1.grok.text_analysis import analyze_text
#from solutions.phase1.claude.text_analysis import analyze_text
#from solutions.phase1.chatgpt.text_analysis import analyze_text
#from solutions.phase1.gemini.text_analysis import analyze_text


#from solutions.phase2.grok.text_analysis import analyze_text
#from solutions.phase2.claude.text_analysis import analyze_text
#from solutions.phase2.chatgpt.text_analysis import analyze_text
#from solutions.phase2.gemini.text_analysis import analyze_text

def test_simple_sentence():
    assert analyze_text("Hello world.") == {
        "characters": 12,
        "words": 2,
        "sentences": 1
    }

def test_multiple_sentences():
    assert analyze_text("Hello world. How are you?") == {
        "characters": 25,
        "words": 5,
        "sentences": 2
    }

def test_without_sentence():
    assert analyze_text("Hello world") == {
        "characters": 11,
        "words": 2,
        "sentences": 0
    }

def test_empty_sentence():
    assert analyze_text("") == {
        "characters": 0,
        "words": 0,
        "sentences": 0
    }

def test_text_with_extra_spaces():
    assert analyze_text("  Hello   world.  ") == {
        "characters": 18,
        "words": 2,
        "sentences": 1
    }

def test_only_spaces():
    assert analyze_text("     ") == {
        "characters": 5,
        "words": 0,
        "sentences": 0
    }

def test_single_word():
    assert analyze_text("Hello") == {
        "characters": 5,
        "words": 1,
        "sentences": 0
    }

def test_consecutive_sentence_symbols():
    assert analyze_text("Hello!?.") == {
        "characters": 8,
        "words": 1,
        "sentences": 1
    }

def test_invalid_input_none():
    assert analyze_text(None) == False

def test_invalid_input_wrong_type1():
    assert analyze_text(123) == False

def test_invalid_input_wrong_type2():
    assert analyze_text(["Hi"]) == False

