from pathlib import Path
import re
from typing import Dict, Iterable, List, Optional, Tuple


def load_text(file_path: Path) -> str:
    """Return the full text contents of a file."""
    return Path(file_path).read_text(encoding="utf-8")


def tokenize(text: str) -> List[str]:
    """Normalize text and split it into lowercase word tokens."""
    return re.findall(r"[a-z0-9']+", text.lower())


def count_words(words: Iterable[str]) -> Dict[str, int]:
    """Count how many times each word appears.

    Accepts any iterable of string tokens and returns a mapping
    from token to count.
    """
    word_count: Dict[str, int] = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def top_n_words(word_counts: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    """Return the top n words sorted by frequency, then alphabetically."""
    if n <= 0:
        return []
    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:n]


def get_top_n(word_counts: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    """Backward-compatible wrapper used by the tests."""
    return top_n_words(word_counts, n)


def describe_text(word_counts: Dict[str, int]) -> Dict[str, object]:
    """Compute one extra insight about the dataset.

    Returns total words, unique words, most frequent word (word, count)
    and lexical diversity rounded to 2 decimal places.
    """
    total_words = sum(word_counts.values())
    unique_words = len(word_counts)
    most_frequent: Optional[Tuple[str, int]] = (
        top_n_words(word_counts, 1)[0] if word_counts else None
    )
    lexical_diversity = round(unique_words / total_words, 2) if total_words else 0.0

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "most_frequent": most_frequent,
        "lexical_diversity": lexical_diversity,
    }


def main(argv: Optional[Iterable[str]] = None) -> None:
    """Run the word-frequency analysis on the sample dataset or provided file.

    Accepts an optional argument list for easier testing. By default it reads
    `data/sample.txt` and prints the top 5 words.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Data Detective: word frequency report")
    parser.add_argument(
        "--file",
        "-f",
        default=None,
        help="Path to a text file to analyze (default: data/sample.txt)",
    )
    parser.add_argument(
        "--top",
        "-n",
        type=int,
        default=5,
        help="Number of top words to show (default: 5)",
    )
    args = parser.parse_args(args=list(argv) if argv is not None else None)

    project_root = Path(__file__).resolve().parents[1]
    data_path = Path(args.file) if args.file else project_root / "data" / "sample.txt"

    text = load_text(data_path)
    words = tokenize(text)
    counts = count_words(words)
    top_words = top_n_words(counts, args.top)
    summary = describe_text(counts)

    print("=== Data Detective Report ===")
    print(f"Dataset: {data_path.name}")

    if not words:
        print("\nThe file is empty, so there are no words to analyze.")
        return

    print(f"\nTop {args.top} words:")
    for index, (word, count) in enumerate(top_words, start=1):
        print(f"{index}. {word}: {count}")

    print("\nExtra insight:")
    if summary["most_frequent"]:
        mf_word, mf_count = summary["most_frequent"]
        print(f"- Most frequent word: {mf_word} ({mf_count} times)")
    else:
        print("- Most frequent word: None")

    print(f"- Total words: {summary['total_words']}")
    print(f"- Unique words: {summary['unique_words']}")
    print(f"- Lexical diversity: {summary['lexical_diversity']}")


if __name__ == "__main__":
    main()