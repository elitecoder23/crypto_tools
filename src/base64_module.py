"""Base64 encoding/decoding helpers."""

import base64
import binascii


def encode(text: str) -> str:
    """Encode a plaintext string as base64."""

    text_bytes = text.encode("utf-8")
    encoded_bytes = base64.b64encode(text_bytes)
    return encoded_bytes.decode("ascii")


def decode(encoded_text: str) -> str:
    """Decode a base64 string back to plaintext."""

    try:
        decoded_bytes = base64.b64decode(encoded_text.encode("ascii"), validate=True)
    except (binascii.Error, UnicodeEncodeError) as exc:
        raise ValueError("Invalid base64 input") from exc

    try:
        return decoded_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("Decoded bytes are not valid UTF-8") from exc
