import magic

# File path
file_path = 'LostPassport'

# Use magic to identify the file type
file_type = magic.from_file(file_path, mime=True)
file_type
