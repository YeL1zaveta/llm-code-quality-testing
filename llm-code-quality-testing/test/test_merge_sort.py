from solutions.phase1.grok.merge_sort import merge_sort
#from solutions.phase1.claude.merge_sort import merge_sort
#from solutions.phase1.chatgpt.merge_sort import merge_sort
#from solutions.phase1.gemini.merge_sort import merge_sort


#from solutions.phase2.grok.merge_sort import merge_sort
#from solutions.phase2.claude.merge_sort import merge_sort
#from solutions.phase2.chatgpt.merge_sort import merge_sort
#from solutions.phase2.gemini.merge_sort import merge_sort

def test_sort_basic():
    assert merge_sort([3, 2, 1]) == [1, 2, 3]

def test_sort_multiple_elements():
    assert merge_sort([1, 4, 2, 7, 6, 5, 3, 9, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_sort_large_input():
    assert merge_sort(list(range(100, 0, -1))) == list(range(1, 101))

def test_sort_already_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_single_element():
    assert merge_sort([2]) == [2]

def test_sort_empty_list():
    assert merge_sort([]) == []

def test_sort_with_negative_numbers():
    assert merge_sort([-1, 2, 4, -6, -9, 0]) == [-9, -6, -1, 0, 2, 4]

def test_sort_all_negative_numbers():
    assert merge_sort([-1, -2, -3, -4, -5, -6, 0]) == [-6, -5, -4, -3, -2, -1, 0]

def test_sort_all_duplicates():
    assert merge_sort([1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1]

def test_sort_with_duplicates():
    assert merge_sort([1, 2, 2, 2, 3, 3, 3, 4, 4, 1, 9, 9, 5]) == [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 9, 9]

def test_sort_mixed_types():
    assert merge_sort([1, "a", 3]) == False

def test_sort_none_element():
    assert merge_sort([None]) == [None]

def test_sort_string_list():
    assert merge_sort(["a", "b", "c", "d"]) == False