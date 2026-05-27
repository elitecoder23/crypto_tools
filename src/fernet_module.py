import os
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = "secret.key" # make sure 'secret.key' is in .gitignore file so it isn't committed to github

def generate_key() -> bytes:
    """Generate new Fernet encryption key"""
    return Fernet.generate_key() # base64 encoded 32 byte key

def save_key(key: bytes, path: str = KEY_FILE) -> None:
    """Save encryption key to a file"""
    with open(path, "wb") as f: # 'wb' means binary mode
        f.write(key)


def load_key(path: str = KEY_FILE) -> bytes:
    """Load an encryption key from a file"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Key file not found: {path}")
    with open(path, "rb") as f: # 'rb' means reading in binary mode, the keys are bytes not string
        return f.read()
    
def encrypt(plaintext: str, key: bytes) -> str:
    """encrypt a plaintext string using a Fernet key"""
    fernet = Fernet(key)
    encrypted_bytes = fernet.encrypt(plaintext.encode("utf-8"))
    return encrypted_bytes.decode("ascii")

def decrypt(ciphertext: str, key: bytes) -> str:
    """Decrypt a fernet-encrypted string using the original key"""
    try:
        fernet = Fernet(key)
        decrypted_bytes = fernet.decrypt(ciphertext.encode("ascii"))
        return decrypted_bytes.decode("utf-8")
    except InvalidToken: # InvalidToken is Fernet's exception for wrong key or tampered ciphertext
        raise ValueError("Decryption failed: invalid key or corrupted ciphertext")
    


