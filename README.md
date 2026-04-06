# P1: Data Detective

## Summary
This project loads a text file, normalizes and tokenizes the text, counts word
frequencies, reports the top N most common words, and identifies the longest word
that appears only once in the text.

## Dataset
- *File:* data/wagner.txt  
- *Source:* Project Gutenberg — https://www.gutenberg.org/ebooks/52091  
- *Why I chose it:*  
*My Life — Volume 1* by Richard Wagner is a public-domain autobiography written by
the famous German composer. Unlike fictional novels, this text provides a personal
narrative of Wagner’s early life, experiences, and artistic development. The writing
style is more formal and reflective, containing long sentences and descriptive
language. This makes it interesting for analysis because the vocabulary includes both
common words and rare, expressive terms. The dataset allows meaningful insights into
how autobiographical texts differ from fictional works in terms of word usage and
frequency patterns.

## How to run
python -m pytest -q  
python -m src.project

## Approach
- Load the raw text from a UTF-8 file using `Path.read_text()`
- Normalize: convert all text to lowercase, remove punctuation, and collapse extra whitespace
- Tokenize: split the cleaned text into a list of individual words
- Count frequencies: use a dictionary to count occurrences of each word
- Find top N: sort by frequency (descending) and alphabetically for ties, then return top N
- Extra insight: identify all words that appear once and return the longest among them

## Complexity

### count_words
- *Time:* O(n) — one pass through the list of words  
- *Space:* O(u) — storing counts for each unique word  
- *Why:* Each word is processed once and dictionary operations (lookup and update)
are O(1) on average, resulting in linear time complexity.

### top_n_words
- *Time:* O(u log u) — sorting unique words dominates  
- *Space:* O(u) — storing all word-count pairs before slicing  
- *Why:* The sorting step uses Python’s Timsort algorithm, which runs in
O(u log u), and this dominates the total cost compared to slicing.

## Edge-case checklist
- [x] *Empty file* — returns empty results without crashing; extra_insight returns ""  
- [x] *Punctuation-heavy input* — punctuation removed during normalization  
- [x] *Repeated words* — correctly counted using dictionary accumulation  
- [x] *Uppercase/lowercase differences* — normalized to lowercase before counting  
- [x] **n <= 0** — returns an empty list safely  

## Assistance & sources
- *AI used?* Yes  
- *What it helped with:* Understanding code structure, fixing syntax errors,
and improving explanations for complexity and design  
- *Other sources:* Project Gutenberg (https://www.gutenberg.org) for dataset  

## Design note (150–250 words)
I chose *My Life — Volume 1* by Richard Wagner because it provides a different type
of dataset compared to fictional novels. As an autobiography, the text reflects
personal experiences, thoughts, and historical context, which results in a more
formal and descriptive writing style. This makes the analysis interesting because
the most frequent words reveal patterns of narration rather than dialogue or action.

The design of the program follows a modular approach, where each function is
responsible for a single task. For example, normalization handles text cleaning,
tokenization splits the text, and counting tracks word frequency. This separation
makes the code easier to test and debug. One challenge I encountered was ensuring
that punctuation removal did not affect readability while still producing accurate
results. For example, removing hyphens can combine words, but this was acceptable
for the purpose of analysis.

The extra insight I implemented is finding the longest word that appears only once
in the text. This helps highlight rare and complex vocabulary used by Wagner,
providing deeper understanding of his writing style. As a future improvement, I
would add stop-word filtering to remove very common words like “the” and “and” so
that the results focus more on meaningful and unique terms.