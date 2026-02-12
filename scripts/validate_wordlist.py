import sys
import unicodedata
import os

def validate(input_file="words.txt"):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    errors = []
    print(f"Validating {input_file}...")
    
    try:
        with open(input_file, "rb") as f:
            content = f.read()
            content.decode("utf-8")
    except UnicodeDecodeError as e:
        errors.append(f"UTF-8 Encoding Error: {e}")

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    last_word = ""
    seen_words = set()

    for i, line in enumerate(lines):
        word = line.strip()
        if not word:
            continue
            
        if word != unicodedata.normalize("NFC", word):
            errors.append(f"Line {i+1}: Word '{word}' is not in NFC form.")

        if word in seen_words:
            errors.append(f"Line {i+1}: Duplicate word found: '{word}'.")
        seen_words.add(word)

        if word < last_word:
            errors.append(f"Line {i+1}: Sorting issue. '{word}' comes after '{last_word}'.")
        
        last_word = word

    if errors:
        print("\nValidation Failed!")
        for error in errors[:10]:
            print(f" - {error}")
        if len(errors) > 10:
            print(f" ... and {len(errors) - 10} more errors.")
        sys.exit(1)
    else:
        print("Validation Passed! All words are UTF-8, NFC-normalized, unique, and sorted.")

if __name__ == "__main__":
    validate()
