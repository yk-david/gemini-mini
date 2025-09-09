import os
from .config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_directory = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_file_path, 'r') as f:
            content = f.read()

            if len(content) > MAX_CHARS:
                return f'{content[:MAX_CHARS]} [...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    
    except Exception as e:
        return f'Error: {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name='get_file_content', 
    description='Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory', 
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'file_path': types.Schema(
                type=types.Type.STRING, 
                description='The path to the file whose content should be read, relative to the working directory.'
            )
        }, 
        required=['file_path']
    )
)