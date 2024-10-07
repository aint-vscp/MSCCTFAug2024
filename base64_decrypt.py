import base64

def base64_to_text(base64_string):
    try:
        base64_bytes = base64_string.encode('utf-8')
        text_bytes = base64.b64decode(base64_bytes)
        text = text_bytes.decode('utf-8')
        return text
    except Exception as e:
        print(f"Error in base64_to_text: {e}")
        return None

original_base64_text = "VE1DVEZ7RDNyM3owfQ=="

decoded_text = base64_to_text(original_base64_text)
print(f"Decoded Text: {decoded_text}")
