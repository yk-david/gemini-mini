from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file_content import write_file

def call_function(function_call_part, verbose=False):
    args = function_call_part.args or {}
    if verbose:
        if isinstance(function_call_part.args, dict):
            print(f'Calling function: {function_call_part.name}({args})')
    else:
        print(f' - Calling function: {function_call_part.name}')
    
    FUNCTIONS = {
        'get_file_content': get_file_content, 
        'get_files_info': get_files_info, 
        'run_python_file': run_python_file, 
        'write_file_content': write_file
    }