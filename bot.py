import os
import logging
from pprint import pprint

import tweepy
from dotenv import load_dotenv

# Start logging
logger = logging.getLogger("Tweepy")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="tweepy.log")
logger.addHandler(handler)

# Load values from the .env file
load_dotenv()

print(os.getenv("ENV_TEST")) # Check if the .env file is loaded

# Load all the environmental variables into constants
# CONSUMER KEY is the API key
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# To make sure I don't start the program erroneously
input("Press ENTER to start the server...") # Remove this in prod

client = tweepy.Client(
    bearer_token = BEARER_TOKEN,
    consumer_key = CONSUMER_KEY, # API key
    consumer_secret = CONSUMER_SECRET, # API secret
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET,
)

xkaubu = client.get_user(username="xkaubu")
print(f"xkaubu obj: {xkaubu}\n")
xkaubu_id = xkaubu.data.id
print(f"xkaubu's Twitter ID is {xkaubu_id}")