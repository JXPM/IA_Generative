from google import genai
import os

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)