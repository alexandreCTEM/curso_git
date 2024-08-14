import hashlib

def calculate_md5_hash(string):
    md5_hash = hashlib.md5(string.encode()).hexdigest()
    return md5_hash

def main():
    string = "Hello, World!"
    md5_hash = calculate_md5_hash(string)
    print(f"MD5 Hash: {md5_hash}")

if __name__ == "__main__":
    main()

# Run the app
