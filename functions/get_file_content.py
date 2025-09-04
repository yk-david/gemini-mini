import os
from .config import MAX_CHARS

def get_file_content(working_directory, file_path):
    target_directory = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)

    if not target_directory.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_directory):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_directory, 'r') as f:
            file_content_string = f.read()

            if len(file_content_string) > MAX_CHARS:
                return f'{file_content_string[:MAX_CHARS]} [...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    
    except Exception as e:
        return f'Error: {e}'
    
