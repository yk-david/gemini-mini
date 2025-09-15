from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file_content import write_file_content


def call_function(function_call_part, verbose=False):
    func_name = function_call_part.name
    func_args = dict(function_call_part.args or {})
    func_args['working_directory'] = './calculator'
    
    if verbose:
        print(f'Calling function: {func_name}({func_args})')
    else:
        print(f' - Calling function: {func_name}')

    functions = {
        'get_file_content': get_file_content, 
        'get_files_info': get_files_info, 
        'run_python_file': run_python_file, 
        'write_file_content': write_file_content
    }

    func = functions.get(func_name) # if not `func_name`, it returns None
    if func is None:
        return types.Content(
            role='tool', 
            parts=[
                types.Part.from_function_response(
                    name=func_name, 
                    response={'error': f'Unknown function: {func_name}'}
                )
            ]
        )

    try:
        result = func(**func_args)
    except Exception as e:
        return types.Content(
            role='tool', 
            parts=[
                types.Part.from_function_response(
                    name=func_name, 
                    response={'error': str(e)}
                )
            ]
        )
    else:
        return types.Content(
            role='tool', 
            parts=[
                types.Part.from_function_response(
                    name=func_name, 
                    response={'result': result}
                )
            ]
        )


