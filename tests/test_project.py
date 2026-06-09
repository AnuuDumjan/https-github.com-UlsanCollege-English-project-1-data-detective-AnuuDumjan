from src.project import tokenize, count_words, get_top_n, top_n_words

def test_count_words_normal():
    words = ["hello", "world", "hello"]
    result = count_words(words)
    assert result["hello"] == 2
    assert result["world"] == 1

def test_empty_input():
    words = []
    result = count_words(words)
    assert result == {}

def test_case_handling():
    words = tokenize("Hello hello")
    result = count_words(words)
    assert result["hello"] == 2

def test_top_n():
    words = ["a", "b", "a", "c", "a", "b"]
    counts = count_words(words)
    top = get_top_n(counts, 1)
    assert top[0][0] == "a"


def test_top_n_non_positive():
    counts = {"a": 3, "b": 2}
    assert top_n_words(counts, 0) == []
    assert top_n_words(counts, -1) == []


def test_top_n_tie_breaks_alphabetically():
    counts = {"banana": 2, "apple": 2, "carrot": 1}
    assert top_n_words(counts, 2) == [("apple", 2), ("banana", 2)]