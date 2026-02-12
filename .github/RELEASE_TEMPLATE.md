# Release Notes - v1.0.0

## What's New

- Initial release of the comprehensive Nepali Wordlist Dataset.
- **123,363 unique words** extracted from the _Nepali Brihat Sabdakosh_.
- Available formats: `.txt`, `.json`, `.csv`, `.lst`.
- Full documentation and validation scripts.

## Data Integrity

- **SHA-256 Checksums:** Included in `checksums.txt`.
- **Validation:** All words verified for UTF-8 encoding, NFC normalization, and correct sorting.

## How to Verify

Download the `checksums.txt` file and run:

```bash
sha256sum -c checksums.txt
```

---

[View full dataset documentation](https://github.com/bisug/Nepali-Wordlist-Dataset)
