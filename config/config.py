from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("URL_DATABASE")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")