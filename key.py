import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("consumer_key")
CONSUMER_SECRET = os.environ.get("consumer_secret")
ACCESS_TOKEN = os.environ.get("access_token")
ACCESS_TOKEN_SECRET = os.environ.get("access_token_secret")



