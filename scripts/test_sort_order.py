import sys
import os


def test_sort(input_file="words.txt"):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        original = [line.strip() for line in f if line.strip()]

    print("Checking sort order...")
    
    expected = sorted(original)
    
    if original == expected:
        print("Sort Order Check: PASS (Binary/Codepoint Order)")
    else:
        print("Sort Order Check: FAIL (Binary/Codepoint Order)")
        for i in range(len(original)):
            if original[i] != expected[i]:
                print(f"First error at index {i}: Found '{original[i]}', expected '{expected[i]}'")
                break
        sys.exit(1)

if __name__ == "__main__":
    test_sort()
