import base64


def decode_base64(encoded_str: str) -> str:
    """Decode a base64 string to utf-8 string"""
    return base64.b64decode(encoded_str).decode('utf-8')