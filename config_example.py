import os


# Set the Twitter credentials
twitter = dict(
    key = os.environ.get('TWITTER_KEY', ''),
    secret = os.environ.get('TWITTER_SECRET', ''),
    access_token = os.environ.get('TWITTER_TOKEN', ''),
    access_token_secret = os.environ.get('TWITTER_TOKEN_SECRET', '')
)
