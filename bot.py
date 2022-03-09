# System imports
import os
import time
import random

# Third part imports
import tweepy
from dotenv import load_dotenv
from emoji import UNICODE_EMOJI

# Local modules
import keep_alive

# Load values from the .env file
load_dotenv()

print(os.getenv("ENV_TEST")) # Check if the .env file is loaded, comment this out if you don't have this

# Load all the environmental variables into constants
# CONSUMER KEY is the API key
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

## CONSTANTS ##
DEBUG = True
# Verifies if the user wants to continue, this is for development
VERIFY_INPUT = False
# The current directory where it selects current.txt at
# This is used to sort different bots using the same source code
# You can change this to an environmental variable to host the same project with different outputs
BOT_DIR = "kaubu"
# BOT_DIR = os.getenv("BOT_DIR")
TWEET_FILE = f"tweets/{BOT_DIR}/current.txt" # Rename current.txt and replace it to update tweet list
# Message interval in minutes
# Default = 60: every 60 minutes/1 hour
INTERVAL = 10
# Tweet sent out when the bot runs out of messages
RELOAD_MESSAGE = "oi mate @xkaubu @nannowasright, reload the bot"
# Whether the bot will really send messages
# This is good if you just want to test generation
SEND_MESSAGES = True
REPLIT_KEEP_ALIVE = False
FAIL_ON_ERROR = False # Should the bot shutdown whenever it occurs an error?

## BE CAREFUL WHEN CHANGING ME ##
# When you want to manually set seconds for debug purposes
# Be careful doing this without setting SEND_MESSAGES to False
# otherwise it could spam more than the API rate limits allow.
# 
# interval_secs = 2
interval_secs = INTERVAL * 60 # seconds = minutes * 60
## BE CAREFUL WHEN CHANGING ME END ##

# Precalculating the sleep message so it doesn't format every time
SLEEP_MESSAGE = f"Sleeping for {interval_secs} seconds/{INTERVAL} minutes..."

# Analyze how many characters it is, counting emojis as two characters, then returning only 280 (278) characters
def return_200_chars(tweet):
    if len(tweet) <= 280: return tweet
    
    num_emoji = sum(tweet.count(emoji) for emoji in UNICODE_EMOJI)
    ignored_chars = UNICODE_EMOJI.copy()
    ignored_chars['\n'] = 0
    num_other = sum(0 if char in ignored_chars else 1 for char in tweet)
    
    total_chars = (num_emoji*2)+num_other
    if DEBUG: print(f"{tweet}: {total_chars} characters")

    to_cut = 280 - num_other - (num_emoji*2) - 2 # Cut off two extra for safety
    return tweet[:to_cut]

# To make sure I don't start the program erroneously
if VERIFY_INPUT: input("Press [ENTER] to start authentication:")

# Sign in with API V2 credentials
client = tweepy.Client(
    bearer_token = BEARER_TOKEN,
    consumer_key = CONSUMER_KEY, # API key
    consumer_secret = CONSUMER_SECRET, # API secret
    access_token = ACCESS_TOKEN,
    access_token_secret = ACCESS_TOKEN_SECRET,
)

# Sets the user agent
client.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"

tweets = []

print(f"Opening {TWEET_FILE}...")
with open(TWEET_FILE, "r") as f:
    print("Reading lines...")
    lines = f.read()
    print("Splitting lines...")
    tweets = lines.splitlines()

if VERIFY_INPUT: input("Press [ENTER] to start main loop:")

random.shuffle(tweets)

# Turn on web server to keep it hosted
if REPLIT_KEEP_ALIVE:
    keep_alive.keep_alive()

for tweet in tweets:
    if DEBUG: print("Selecting new tweet...")

    if tweet == "": tweet = "<tweet was empty>" # An empty tweet can crash the whole program
    if DEBUG: print(f"Tweet:\t\t\t{tweet}")
    tweet = return_200_chars(tweet)
    if DEBUG: print(f"Cut tweet:\t\t{tweet}")
    print("Sending tweet...")
    try:
        if SEND_MESSAGES: client.create_tweet(
            text=tweet
            # user_auth is True by default
        )
    except Exception as e:
        print(f"[ERROR] {e}")
        if FAIL_ON_ERROR: break
    
    if DEBUG: print(SLEEP_MESSAGE)
    time.sleep(interval_secs) # Minutes x 60 to get seconds

print("Sending shutdown...")
if SEND_MESSAGES: client.create_tweet(
    text=RELOAD_MESSAGE
)