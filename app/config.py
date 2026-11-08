
import os
from pathlib import Path
from dotenv import load_dotenv

# Locate the .env file in the project root
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "campus_app"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "campus_marketplace")
}
