import hashlib
import os
import hmac


def hash_md5(text: str) -> str:
    """Hash a string using md5, obviously dont use this for actual security"""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def hash_sha1(text: str) -> str:
    """Hash a string using sha1"""
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def hash_sha256(text: str) -> str:
    """Hash a string using sha256"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def hash_with_salt(password: str, salt: bytes | None = None) -> tuple[str, str]:
    """hash a password with a random salt using sha256"""
    if salt is None:
        salt = os.urandom(32)

    salted = salt + password.encode("utf-8")
    hex_hash = hashlib.sha256(salted).hexdigest()
    hex_salt = salt.hex()
    return hex_hash, hex_salt


def verify_password(password: str, hex_hash: str, hex_salt: str) -> bool:
    """verify a password against a stored hash and salt"""
    salt = bytes.fromhex(hex_salt)
    candidate_hash, _ = hash_with_salt(password, salt=salt)
    return hmac.compare_digest(candidate_hash, hex_hash)
