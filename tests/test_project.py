from src.project import (
    count_words,
    normalize_text,
    tokenize,
    top_n_words,
    load_text,
)


# --- normalize_text ---

def test_normalize_text_wagner_style() -> None:
    text = "Richard Wagner, THE Composer!"
    assert normalize_text(text) == "richard wagner the composer"


# --- tokenize ---

def test_tokenize_wagner_sentence() -> None:
    text = "richard wagner was a composer"
    assert tokenize(text) == ["richard", "wagner", "was", "a", "composer"]


# --- count_words ---

def test_count_words_wagner_example() -> None:
    words = ["wagner", "music", "wagner"]
    assert count_words(words) == {"wagner": 2, "music": 1}


# --- top_n_words ---

def test_top_n_words_wagner_counts() -> None:
    counts = {"wagner": 5, "music": 2, "life": 3}
    assert top_n_words(counts, 2) == [("wagner", 5), ("life", 3)]


def test_top_n_words_zero_n() -> None:
    counts = {"wagner": 5}
    assert top_n_words(counts, 0) == []


# --- load_text (real file test) ---

def test_load_text_wagner_file_exists() -> None:
    text = load_text("data/wagner.txt")
    assert isinstance(text, str)
    assert len(text) > 0