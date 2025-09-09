import os
import sys
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working direcoty'
        
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        completed = subprocess.run(
            ['python', file_path, *args], 
            cwd=working_directory, 
            capture_output=True, 
            text=True, 
            timeout=30
        )

        stdout = completed.stdout or ''
        stderr = completed.stderr or ''

        if not stdout and not stderr:
            return 'No output produced.'
        
        parts = []
        if stdout:
            parts.append(f'STDOUT: {stdout}')
        if stderr:
            parts.append(f'STDERR: {stderr}')
        if completed.returncode != 0:
            parts.append(f'Process exited with code {completed.returncode}')
        
        return '\n'.join(parts)


    except Exception as e:
        return f'Error: executing Python file: {e}'
                                        

schema_run_python_file = types.FunctionDeclaration(
    name='run_python_file', 
    description='Run a Python file within the working directory and return stdout/stderr and exit code.', 
    parameters=types.Schema(
        type=types.Type.OBJECT, 
        properties={
            'file_path': types.Schema(
                type=types.Type.STRING, 
                description='Path to the Python file to execute, relative path to the working directory.'
            ), 
            'args': types.Schema(
                type=types.Type.ARRAY, 
                items=types.Schema(
                    type=types.Type.STRING, 
                    description='Optional arguments to pass to the Python file.'
                ), # REQUIRED for arrays
                description='Optional arguments to pass to the Python file.'
            )
        }, 
        required=['file_path']
    )
)