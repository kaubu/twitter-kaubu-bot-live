# twitter-kaubu-bot-live
This is the source code for my bot that tweets out AI-generated tweets based off of my tweets.

The bot is available at [@kaubuBOT](https://twitter.com/xkaubuBOT)

## Setup
Install these dependencies:

`pip install tweepy python-dotenv emoji`

There already exists an example `.env.example` file.

Rename the file to `.env`. The file should look like this:

```
BEARER_TOKEN=

# Consumer/API keys
CONSUMER_KEY=
CONSUMER_SECRET=

ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=

ENV_TEST=.env has been loaded
```

Then, enter in your secrets there, or enter it in your environment.