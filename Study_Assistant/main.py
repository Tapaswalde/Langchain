import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Create the Study Assistant function
def study_assistant(user_prompt):
    """
    Sends a prompt to the Gemini model and gets a response.
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_prompt
    )
    return response.text

# Un-indented so this actually runs when you start the script
user_question = input("Please enter your query: ")
result = study_assistant(user_question)
print(result)
