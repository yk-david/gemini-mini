import os
from google.genai import types

def get_files_info(working_directory, directory='.'):
    target_directory = os.path.join(working_directory, directory)
    abs_working_directory = os.path.abspath(working_directory)

    if not os.path.abspath(target_directory).startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory' # There still could be `directory` inside other directory than `working_directory`, but it would mean it's not permitted.
    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'
    
    item_description = []
    
    for item in os.listdir(target_directory):
        item_description.append(
            f'- {item}: file_size={os.path.getsize(os.path.join(target_directory, item))} bytes, is_dir={os.path.isdir(os.path.join(target_directory, item))}'
        )
        
    try:
        if item_description:
            return f'Result for "{directory}" directory:\n{'\n'.join(item_description)}'
    except:
        Exception("There isn't item in the directory")


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