from src.base64_module import encode, decode
from src.hash_module import (
    hash_md5,
    hash_sha1,
    hash_sha256,
    hash_with_salt,
    verify_password,
)
from src.fernet_module import generate_key, save_key, load_key, encrypt, decrypt


def print_menu() -> None:
    """Display the main menu"""
    print("\n=== Crypto Tool ===")
    print("1. Base64 encode")
    print("2. Base64 decode")
    print("3. Hash a string (MD5 / SHA1 / SHA256)")
    print("4. Hash a password with salt")
    print("5. Verify a password against a hash")
    print("6. Generate and save a Fernet key")
    print("7. Encrypt a message")
    print("8. Decrypt a message")
    print("9. Exit")
    print("===================")


def handle_base64_encode() -> None:
    """Handle Base64 encode option"""
    text = input("Enter text to encode: ")
    print(f"Encoded: {encode(text)}")


def handle_base64_decode() -> None:
    """Handle Base64 decode option"""
    text = input("Enter Base64 value to decode to plaintext: ")
    try:
        print(f"Decoded: {decode(text)}")
    except ValueError as e:
        print(f"Error: {e}")


def handle_hash() -> None:
    """Handle the hashing option"""
    text = input("Enter the text to hash: ")
    print(f"MD5: {hash_md5(text)}")
    print(f"SHA1: {hash_sha1(text)}")
    print(f"SHA256: {hash_sha256(text)}")


def handle_salted_hash() -> None:
    """Handle salted password hashing option"""
    password = input("Type in your password to hash: ")
    hex_hash, hex_salt = hash_with_salt(password)
    print(f"Hash: {hex_hash}")
    print(f"Salt: {hex_salt}")
    print("Store both the hash and the salt to verify later")


def handle_password_verification() -> None:
    """Handle password verification option"""
    password = input("Type in your password to be verified: ")
    hex_hash = input("Enter stored hash: ")
    hex_salt = input("Enter stored salt: ")

    try:
        result = verify_password(password, hex_hash, hex_salt)
        print("Password match: True" if result else "Password match: False")
    except ValueError as e:
        print(f"Error: {e}")


def handle_generate_key() -> None:
    """Handle the fernet key generation"""
    key = generate_key()
    save_key(key)
    print("Key generated and saved to secret.key file")


def handle_encrypt() -> None:
    """Handle message encryption option"""
    try:
        key = load_key()
        message = input("Enter message to encrypt: ")
        print(f"Here is your encrypted message: {encrypt(message, key)}")
    except FileNotFoundError as e:
        print(f"Error: {e} -- run option 6 first to generate a key")
    except ValueError as e:
        print(f"Error: {e}")


def handle_decrypt() -> None:
    """Handle message decryption option"""
    try:
        key = load_key()
        ciphertext = input("Enter the ciphertext to decrypt: ")
        print((f"Decrypted: {decrypt(ciphertext, key)}"))
    except FileNotFoundError as e:
        print(f"Error: {e} --- run option 6 first to generate a key")
    except ValueError as e:
        print(f"Error: {e}")


MENU_ACTIONS = {
    "1": handle_base64_encode,
    "2": handle_base64_decode,
    "3": handle_hash,
    "4": handle_salted_hash,
    "5": handle_password_verification,
    "6": handle_generate_key,
    "7": handle_encrypt,
    "8": handle_decrypt,
}


def main() -> None:
    """Main entry point for the crypto tool"""
    while True:
        print_menu()
        choice = input("Select an option (1-9): ").strip()
        if choice == "9":
            print("Goodbye")
            break
        action = MENU_ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please select from 1-9")


if __name__ == "__main__":
    main()
