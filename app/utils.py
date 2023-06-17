def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def validate_hex_code(hex_code):
    if len(hex_code) != 7 or hex_code[0] != "#":
        return False
    try:
        int(hex_code[1:], 16)
        return True
    except ValueError:
        return False

def validate_input_payload(payload):
    if not isinstance(payload, dict):
        return False

    if "colors" not in payload or "categories" not in payload or "threshold" not in payload:
        return False

    if not isinstance(payload["colors"], list) or not isinstance(payload["categories"], dict) or not isinstance(payload["threshold"], (int, float)):
        return False

    if not all(validate_hex_code(color) for color in payload["colors"]) or not all(validate_hex_code(category_color) for category_color in payload["categories"].values()):
        return False

    return True

from numpy import dot
from numpy.linalg import norm

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))