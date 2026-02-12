import json
import csv
import sys
import os

def generate_formats(input_file="words.txt"):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    print(f"Reading {input_file}...")
    with open(input_file, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]

    print("Generating data/words.json...")
    with open("data/words.json", "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

    print("Generating data/words.csv...")
    with open("data/words.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for word in words:
            writer.writerow([word])

    print("Generating data/words.lst...")
    with open("data/words.lst", "w", encoding="utf-8") as f:
        for word in words:
            f.write(word + "\n")

    print("Success! Generated JSON, CSV, and LST formats.")

if __name__ == "__main__":
    generate_formats()
