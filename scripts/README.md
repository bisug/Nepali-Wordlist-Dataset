# Utility Scripts

This directory contains Python scripts for managing and validating the Nepali Wordlist Dataset.

## Requirements

- Python 3.9+
- `requests` (optional, for remote fetching)

## Scripts

### 1. `validate_wordlist.py`

Validates the `words.txt` file for:

- UTF-8 encoding.
- NFC Unicode normalization.
- Uniqueness (no duplicates).
- Consistent sorting.

**Usage:**

```bash
python scripts/validate_wordlist.py
```

### 2. `generate_formats.py`

Generates JSON, CSV, and LST variants from the main `words.txt` file.

**Usage:**

```bash
python scripts/generate_formats.py
```

### 3. `convert_formats.py`

A CLI tool to convert the wordlist to a specific format.

**Usage:**

```bash
python scripts/convert_formats.py words.txt data/output.json --format json
```

### 4. `test_sort_order.py`

Verifies that the words are sorted according to expectations.
