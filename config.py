import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Config:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
