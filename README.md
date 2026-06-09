# P1: Data Detective

Summary
This project analyzes a text file, counts word frequencies, shows the top N words, and reports one extra insight. In this version, the extra insight is lexical diversity — the ratio of unique words to total words.

Dataset
File: data/sample.txt
Why I chose it: I used a short sports-themed text because it is easy to verify by hand and includes repeated words, punctuation, and mixed sentence structure. That makes it a good small dataset for testing frequency analysis.
How to run
pytest -q
python -m src.project
Usage examples

# Run the unit tests
pytest -q

# Run the report using the bundled sample dataset (top 5 words)
python -m src.project

# Run the report showing the top 3 words for a specific file
python -m src.project --file data/sample.txt --top 3
CLI flags

--file / -f: path to a text file to analyze (default: data/sample.txt)
--top / -n: number of top words to display (default: 5)
Approach
Load text from a file.
Normalize the text by converting it to lowercase.
Tokenize the text into words using regular expressions.
Count word frequencies with a dictionary.
Sort and display the top N words.
Report an extra insight: most frequent word, total words, unique words, and lexical diversity.
Complexity
count_words
Time: O(w)
Space: O(u)
Why: The function visits each word once and stores one count per unique word.
top_n_words
Time: O(u log u)
Space: O(u)
Why: The unique-word dictionary is sorted by frequency, so the sort dominates the running time.
Edge-case checklist
 empty file
 punctuation-heavy input
 repeated words
 uppercase/lowercase differences
 n <= 0
Assistance & sources
AI used? Y
What it helped with: polishing the README, improving edge-case handling, and checking test coverage.
Other sources: Python documentation for re and pathlib.
Design note (150–250 words)
For this project, I selected a short football-themed text file as the dataset. I chose it because it is small enough to check manually, but still includes repeated vocabulary, punctuation, and natural sentence patterns that make frequency analysis meaningful. My main design decision was to keep the program simple and readable: one function loads the file, one tokenizes the text, one counts frequencies, and one returns the top N results. This makes the code easy to test and easy to improve later.

The easiest part of the project was using a dictionary to store word counts, because that matches the problem directly and runs efficiently. The harder part was making the behavior reliable for edge cases such as empty files, capitalization differences, punctuation-heavy input, and invalid values like n <= 0. I also wanted the output to look clear when the program is run from the command line.

If I were improving the project next, I would let the user choose any text file from the command line and add a simple bar chart of the most frequent words for a more visual presentation.

