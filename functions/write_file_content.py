import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f'Error: creating directory: {e}'
        
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: writing to file: {e}'
    

schema_write_file = types.FunctionDeclaration(
    name='write_file',
    description='Write file to the specific path and constrained to the working directory.', 
    parameters=types.Schema(
        type=types.Type.OBJECT, 
        properties={
            'file_path': types.Schema(
                type=types.Type.STRING, 
                description='The path to the file, relative to the working directory. Handle errors when it occurs.'
            ), 
            'content': types.Schema(
                type=types.Type.STRING, 
                description='Content to be written in the file'
            )
        }
    ) 
)

"""
schema_get_files_info = types.FunctionDeclaration(
    name='get_files_info', 
    description='Lists files in the specified directory along with their sizes, constrained to the working directory.', 
    parameters=types.Schema(
        type=types.Type.OBJECT, 
        properties={
            'directory': types.Schema(
                type=types.Type.STRING, 
                description='The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.'
            )
        }
    )
)
"""