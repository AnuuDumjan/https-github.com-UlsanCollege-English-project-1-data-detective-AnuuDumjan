"""
Project 1: Data Detective

Dataset: My Life — Volume 1 by Richard Wagner (Public Domain)
"""

from __future__ import annotations

import string
from pathlib import Path


def load_text(path: str) -> str:
    """Load and return the full text from a UTF-8 file."""
    return Path(path).read_text(encoding="utf-8")


def normalize_text(text: str) -> str:
    """Normalize text:
    - lowercase
    - remove punctuation
    - remove extra spaces
    """
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.split())
    return text


def tokenize(text: str) -> list[str]:
    """Convert text into list of words."""
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count frequency of each word."""
    counts: dict[str, int] = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return top N most frequent words."""
    if n <= 0:
        return []

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> str:
    """
    Return the longest word that appears only once.
    """
    unique_words = []

    for word, count in counts.items():
        if count == 1:
            unique_words.append(word)

    if not unique_words:
        return ""

    return max(unique_words, key=len)


# 🔥 NEW (to make your project different & better)
def average_word_length(words: list[str]) -> float:
    """Return average word length."""
    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def run_demo(path: str, n: int = 10) -> dict[str, object]:
    """Run full analysis."""
    text = load_text(path)
    normalized = normalize_text(text)
    words = tokenize(normalized)
    counts = count_words(words)

    return {
        "total_words": len(words),
        "unique_words": len(counts),
        "top_words": top_n_words(counts, n),
        "longest_unique_word": extra_insight(words, counts),
        "average_word_length": average_word_length(words),  # ⭐ extra feature
    }


if __name__ == "__main__":
    file_path = Path("data/sample.txt")  # ← your book file

    if file_path.exists():
        results = run_demo(str(file_path), 10)

        print("\n--- Analysis Result ---")
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        print("❌ File not found. Put 'wagner.txt' inside data folder.")
        