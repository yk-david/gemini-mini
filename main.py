import os
import sys 
from google import genai
from google.genai import types
from dotenv import load_dotenv
from available_functions import available_functions
from prompts import system_prompt
from functions.call_function import call_function

def main():
    verbose = '--verbose' in sys.argv

    if not len(sys.argv) > 1:
        print('You should provide input.')
        return sys.exit(1)
    
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')

    client = genai.Client(api_key=api_key)
    user_prompt = sys.argv[1]

    messages = [
        types.Content(role='user', parts=[types.Part(text=user_prompt)])
    ]

    loop_count = 0

    while loop_count <= 20:
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash-001', 
                contents=messages, 
                config=types.GenerateContentConfig(
                    tools=[available_functions], 
                    system_instruction=system_prompt
                )
            )

            # add the model's message(s)
            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)
            
            # handle tool calls immediately
            if response.function_calls:
                for function_call in response.function_calls:
                    result = call_function(function_call, verbose)

                    # ensure result contains the function_response payload
                    if not result.parts or not result.parts[0].function_response:
                        raise Exception('empty function call result')
                    
                    # append tool result as a user message
                    messages.append(
                        types.Content(
                            role='user', 
                            parts=[
                                types.Part.from_function_response(
                                    name=function_call.name, 
                                    response=result.parts[0].function_response.response
                                )
                            ]
                        )
                    )

                    if verbose:
                        print(f'- Calling function: {function_call.name}')
                
                # continue loop for next step
                loop_count += 1
                continue
            
            # if no tool calls and we have text, we're done
            if response.text:
                print(response.text)
                break

            loop_count += 1

        except Exception as e:
            if verbose:
                print(f"Error: {e}")
            loop_count +=1

    
    usage_metadata = response.usage_metadata

    if '--verbose' in sys.argv[1:]:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {usage_metadata.prompt_token_count}')
        print(f'Response tokens: {usage_metadata.candidates_token_count}')
    
    


if __name__ == "__main__":
    main()
