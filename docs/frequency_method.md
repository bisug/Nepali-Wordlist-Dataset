# Word Frequency Methodology

The primary `words.txt` file is an unweighted list of unique Nepali words. For applications that require word frequency (e.g., predictive text, language modeling), we recommend the following methodology to generate a frequency-annotated wordlist.

## Recommended Datasets

To obtain realistic frequency scores, you can process large-scale Nepali corpora:

1. **OSCAR (Open Super-large Crawler Aggregated Corpus):** A massive multilingual corpus suitable for training language models.
2. **CC-100:** A dataset of 100 languages (including Nepali) constructed from Common Crawl.
3. **Wikipedia:** Use a dump of Nepali Wikipedia for high-quality formal text.

## Processing Steps

### 1. Tokenization

Use a tokenizer that handles Unicode correctly. For Nepali, simple whitespace splitting followed by punctuation removal is often a good start.

```python
import re

def tokenize(text):
    # Remove punctuation and split by whitespace
    text = re.sub(r'[^\u0900-\u097F\s]', '', text)
    return text.split()
```

### 2. Counting & Normalization

Count the occurrences of each word and normalize the counts into a score (e.g., zipfian or relative frequency).

### 3. Merging with Wordlist

Filter the results to include only words present in our verified `words.txt` to ensure quality.

## Synthetic Frequency (words_freq.csv)

For immediate testing, you can use the synthetic frequency scores provided in some distribution variants, which are estimated based on word length and commonality patterns (e.g., shorter words often having higher frequency).
