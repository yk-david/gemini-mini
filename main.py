import os
import sys 
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    if not len(sys.argv) > 1:
        print('You should provide input.')
        return sys.exit(1)
    
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')

    client = genai.Client(api_key=api_key)
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    user_prompt = sys.argv[1]

    messages = [
        types.Content(role='user', parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages, 
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    usage_metadata = response.usage_metadata

    print(response.text)

    if '--verbose' in sys.argv[1:]:
        print(f'User prompt: {user_prompt}')
        print(f'Prompt tokens: {usage_metadata.prompt_token_count}')
        print(f'Response tokens: {usage_metadata.candidates_token_count}')


if __name__ == "__main__":
    main()
