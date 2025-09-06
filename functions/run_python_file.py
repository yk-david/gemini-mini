import os
import sys
import subprocess

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
                                        



















# import os
# import subprocess

# def run_python_file(working_directory, file_path, args=[]):
#     abs_working_directory = os.path.abspath(working_directory)
#     abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

#     if not abs_file_path.startswith(abs_working_directory):
#         return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
#     if not os.path.exists(abs_file_path):
#         return f'Error: File "{file_path}" not found.'
    
#     if not file_path.endswith('.py'):
#         return f'Error: "{file_path}" is not a Python file.'
    
#     result = subprocess.run(['python', file_path, *args], stdin=None, input=None, stdout=True, stderr=True, capture_output=True, shell=False, cwd=working_directory, timeout=30, check=False, encoding=None, errors=None, text=True, env=None, universal_newlines=True)

#     if result.stdout == '' and result.stderr == '':
#         return 'No output produced.'
#     try:
#         output_message = ''
#         if result.stdout:
#             output_message += f'STDOUT: {result.stdout}'
#         if result.stderr:
#             output_message += f'\nSTDERR: {result.stderr}'
#         if result.returncode != 0:
#             output_message += f'\nProcess exited with code X'
#     except Exception as e:
#         return f'Error: executing Python file: {e}'