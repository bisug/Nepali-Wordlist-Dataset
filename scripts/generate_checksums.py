import hashlib
import os

def generate_checksums():
    files = ["words.txt", "data/words.json", "data/words.csv", "data/words.lst"]
    output_file = "data/checksums.txt"
    
    print(f"Generating checksums for {', '.join(files)}...")
    
    with open(output_file, "w", encoding="utf-8") as out:
        for filename in files:
            if os.path.exists(filename):
                sha256_hash = hashlib.sha256()
                with open(filename, "rb") as f:
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                hash_hex = sha256_hash.hexdigest()
                out.write(f"{hash_hex}  {filename}\n")
                print(f" - {filename}: {hash_hex}")
            else:
                print(f" Warning: {filename} not found.")

    print(f"Checksums saved to {output_file}.")

if __name__ == "__main__":
    generate_checksums()
