# Contributing to the Nepali Wordlist Dataset

Thank you for your interest in improving this dataset! We welcome corrections, new words, and improvements to the automation scripts.

## How to Contribute

### 1. Adding or Correcting Words

- Ensure the word is in **Nepali script** (Devanagari).
- All words must be in **Unicode NFC** normalization form.
- Words should be provided one per line in `words.txt`.
- The list must remain **alphabetically sorted** according to Nepali collation.
- Ensure there are no duplicates.

### 2. Validation

Before submitting a pull request, please run the validation script:

```bash
python scripts/validate_wordlist.py
```

This script checks for UTF-8 encoding, NFC normalization, sorted order, and duplicates.

### 3. Submitting Changes

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your edits to `words.txt`.
4. Run the validation script to ensure data integrity.
5. Commit your changes with a clear message.
6. Submit a Pull Request.

## Code of Conduct

Please be respectful and professional in all interactions.

## License

By contributing to this repository, you agree that your contributions will be licensed under the [CC0 1.0 Universal](LICENSE) license.
