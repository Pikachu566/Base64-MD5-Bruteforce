import base64
import hashlib
import itertools
import string

def encode_password(password):
    base64_encoded = base64.b64encode(password.encode()).decode()
    md5_hashed = hashlib.md5(base64_encoded.encode()).hexdigest()
    return base64_encoded, md5_hashed

def decode_base64(base64_encoded):
    original_password = base64.b64decode(base64_encoded.encode()).decode()
    return original_password

def brute_force_md5(target_hash, max_length=8):
    chars = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            hashed_guess = hashlib.md5(guess.encode()).hexdigest()
            if hashed_guess == target_hash:
                return guess
            print(f"Brute Force Attack: {guess}...")
    return None

def main():
    while True:
        print("\n=== Password Encoder, Decoder & MD5 Brute Force ===")
        print("1. Encode Password (Base64 + MD5)")
        print("2. Decode Base64 to Original Password")
        print("3. Brute Force MD5 Hash")
        print("4. Quit Program")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            password = input("Enter your password: ")
            base64_result, md5_result = encode_password(password)
            print("\nEncoded to Base64:", base64_result)
            print("Hashed to MD5:", md5_result)

        elif choice == "2":
            base64_input = input("Enter Base64 password: ")
            try:
                original_password = decode_base64(base64_input)
                print("\nOriginal Password:", original_password)
            except Exception as e:
                print("\nError decoding Base64:", e)

        elif choice == "3":
            target_hash = input("Enter the MD5 hash for brute force: ")
            print("Brute force process started. Please wait...")
            password = brute_force_md5(target_hash)
            if password:
                print(f"\nThe original password is: {password}")
            else:
                print("\nPassword not found.")

        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
