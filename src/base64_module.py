import base64

def encode(text: str) -> str:
    """encoding a plaintext string to base64"""

    text_bytes = text.encode("utf-8")
    encoded_bytes = base64.b64encode(text_bytes)

    return encoded_bytes.decode("utf-8")

def decode(encoded_text: str) -> str:
    """decode base64 string back to plaintext"""

    encoded_bytes = encoded_text.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_bytes)

    return decoded_bytes.decode("utf-8")


