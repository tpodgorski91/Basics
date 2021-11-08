import os


def oauth():
    return {"consumer_key": os.getenv("TWITTER_KEY"),
            "consumer_secret": os.getenv("TWITTER_SECRET"),
            "token_key": os.getenv("TWITTER_TOKEN2"),
            "token_secret": os.getenv("TWITTER_SECRET_TOKEN")}
