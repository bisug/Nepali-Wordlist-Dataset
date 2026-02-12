import json
import csv
import argparse
import sys
import os

def convert():
    parser = argparse.ArgumentParser(description="Convert wordlist to various formats.")
    parser.add_argument("input", help="Input .txt file")
    parser.add_argument("output", help="Output file path")
    parser.add_argument("--format", choices=["json", "csv", "lst"], help="Output format")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found.")
        sys.exit(1)

    fmt = args.format or args.output.split(".")[-1].lower()

    print(f"Reading {args.input}...")
    with open(args.input, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]

    if fmt == "json":
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(words, f, ensure_ascii=False, indent=2)
    elif fmt == "csv":
        with open(args.output, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            for word in words:
                writer.writerow([word])
    elif fmt == "lst" or fmt == "txt":
        with open(args.output, "w", encoding="utf-8") as f:
            for word in words:
                f.write(word + "\n")
    else:
        print(f"Error: Unsupported format '{fmt}'.")
        sys.exit(1)

    print(f"Successfully converted to {args.output}")

if __name__ == "__main__":
    convert()
