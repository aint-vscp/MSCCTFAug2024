import os

def check_files_for_keyword(folder_path, keyword):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if keyword in content:
                        print(f"Keyword '{keyword}' found in: {file_path}")
            except Exception as e:
                print(f"Could not read file {file_path}. Error: {e}")

folder_path = 'big-zip-files'
keyword = 'picoCTF'
check_files_for_keyword(folder_path, keyword)
