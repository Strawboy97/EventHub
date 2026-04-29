from dotenv import load_dotenv
import os
load_dotenv()
BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise ValueError("BASE_URL is not set in your .env file")