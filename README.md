# Nepali Wordlist Dataset

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-CC0--1.0-green.svg)
![Words](https://img.shields.io/badge/words-123k-orange.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

A comprehensive, curated dataset of **123,363 unique Nepali words** in UTF-8 encoding. This repository is designed for natural language processing (NLP), spell checkers, machine learning, and linguistic research.

### [**Try the Live Search Demo →**](https://bisug.github.io/Nepali-Wordlist-Dataset/)

> _Now with Dark Mode 🌓, English/Nepali UI 🇳🇵, and Instant Copy 📋_

---

## 📋 Table of Contents

- [Statistics](#-statistics)
- [Repository Structure](#-repository-structure)
- [Data Curation](#-data-curation)
- [How to Use](#-how-to-use)
  - [Remote Fetching (Raw)](#remote-fetching-raw)
  - [Code Implementation Examples](#code-implementation-examples)
- [Data Integrity & Validation](#-data-integrity--validation)
- [Contributing](#-contributing)
- [Citation](#-citation)
- [License](#-license)

---

## 📊 Statistics

- **Total Unique Words:** 123,363
- **Primary Encoding:** UTF-8 (NFC Normalization)
- **Formatting:** Plain text, one word per line, alphabetically sorted.
- **Source:** _Nepali Brihat Sabdakosh_ (नेपाली बृहत् शब्दकोश).

---

## 📂 Repository Structure

- `words.txt`: The definitive plain-text wordlist.
- `data/words.json`: Wordlist as a JSON array for web/app integration.
- `data/words.csv`: Wordlist in CSV format (one column).
- `data/words.lst`: Format compatible with Hunspell/Aspell.
- `data/checksums.txt`: SHA-256 hashes for data integrity verification.
- `scripts/`: Python utilities for validation and conversion.
- `docs/`: Web demo and extended documentation.
- `.github/`: Metadata and contribution guidelines.

---

## 🛠 Data Curation

The words were extracted from a structured JSON dump of the _Nepali Brihat Sabdakosh_.

1. **Extraction:** Automated parsing of the dictionary entries.
2. **Normalization:** All words are strictly normalized to **Unicode NFC** form to ensure consistency across platforms.
3. **Cleaning:** Removed duplicates, numerals, and non-Devanagari characters.
4. **Sorting:** The final list is sorted according to Devanagari code points.

<details>
<summary><b>View Data Sample (First/Last 10 words)</b></summary>

**First 10:**

- अ
- अ:
- अआ
- अआत
- अआनार्इ
- अआहो
- अइभरि
- अइकरा
- अइकवार
- अइखल

**Last 10:**

- ह्ला
- ह्लास
- ह्वन
- ह्वब्रिदिज
- ह्वय
- ह्वये
- ह्वयेका
- ह्वर्इ
- ह्वर्र
- ह्वेल
</details>

---

## 🚀 How to Use

### Remote Fetching (Raw)

You can fetch the data directly into your CI/CD pipelines or scripts:

- **Main List:** `https://raw.githubusercontent.com/bisug/Nepali-Wordlist-Dataset/main/words.txt`
- **JSON Variant:** `https://raw.githubusercontent.com/bisug/Nepali-Wordlist-Dataset/main/data/words.json`

### Code Implementation Examples

#### 🐍 Python

```python
import requests
url = "https://raw.githubusercontent.com/bisug/Nepali-Wordlist-Dataset/main/words.txt"
words = requests.get(url).text.splitlines()
print(f"Loaded {len(words)} words.")
```

#### 🟨 JavaScript (Node.js)

```javascript
const axios = require("axios");
const url =
  "https://raw.githubusercontent.com/bisug/Nepali-Wordlist-Dataset/main/words.txt";
axios
  .get(url)
  .then((res) => console.log(`Loaded ${res.data.split("\n").length} words.`));
```

#### 🐹 Go

```go
resp, _ := http.Get("https://raw.githubusercontent.com/bisug/Nepali-Wordlist-Dataset/main/words.txt")
scanner := bufio.NewScanner(resp.Body)
for scanner.Scan() { /* process word */ }
```

---

## 🛡 Data Integrity & Validation

Integrity is guaranteed via SHA-256 checksums. To verify your local files:

```bash
sha256sum -c data/checksums.txt
```

We also recommend running our validation script after any internal modifications:

```bash
python scripts/validate_wordlist.py
```

---

## 🤝 Contributing

Contributions are welcome! Please see [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) for guidelines on how to suggest new words or improvements.

---

## 📝 Citation

If you use this dataset in a research paper or project, please cite it using:

```bibtex
@dataset{nepali_wordlist_2026,
  author = {Bisu Tamang},
  title = {Nepali Wordlist Dataset},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/bisug/Nepali-Wordlist-Dataset}},
}
```

---

## 📜 License

This work is dedicated to the public domain under the **CC0 1.0 Universal** license. See [LICENSE](LICENSE) for details.
