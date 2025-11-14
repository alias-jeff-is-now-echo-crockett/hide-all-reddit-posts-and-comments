import praw
from reddit_api_key import key


# Initialize Reddit instance
reddit = praw.Reddit(
    client_id="your client id",
    client_secret="your client secret",
    user_agent="your user agent",
    username="your reddit username",
    password="your reddit password"
)

