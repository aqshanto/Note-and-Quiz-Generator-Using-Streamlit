import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
my_api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

def debug_genration(code_text):
    prompt = """You have to work in following process
    1. Find the error and give me the error explaination
    2. use this exactly ---Solution With Code--- as it is
    3. give the me the solution of the problem in proper markdown 
    4. give me the correct code in c++ language with proper indentation
    """
    request = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents = [code_text,prompt] 
    )
    return request.text