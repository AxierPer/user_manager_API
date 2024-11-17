from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("URL_DATABASE")