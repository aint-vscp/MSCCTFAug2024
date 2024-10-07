def string_to_bytes(s):
    return s.encode('utf-8')

def bytes_to_big_endian(byte_data):
    return byte_data

def bytes_to_little_endian(byte_data):
    return byte_data[::-1]

# Example word
word = "lhkev"

# Convert the word to bytes
byte_data = string_to_bytes(word)

# Get little-endian and big-endian representations
little_endian_bytes = bytes_to_little_endian(byte_data)
big_endian_bytes = bytes_to_big_endian(byte_data)

print(f"Original bytes: {byte_data.hex()}")
print(f"Little-endian bytes: {little_endian_bytes.hex()}")
print(f"Big-endian bytes: {big_endian_bytes.hex()}")
