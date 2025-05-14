import os
import praw
import tweepy

# Load environment variables
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_user_agent = os.getenv("REDDIT_USER_AGENT")
reddit_username = os.getenv("REDDIT_USERNAME")
reddit_password = os.getenv("REDDIT_PASSWORD")

twitter_api_key = os.getenv("TWITTER_API_KEY")
twitter_api_secret = os.getenv("TWITTER_API_SECRET")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
twitter_access_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Content to post
title = "Discover Natural Migraine Remedies That Actually Work!"
link = "https://soothera.com/blog/latest"  # Update to your blog link
message = f"{title} Read more: {link}"

# Reddit Posting
def post_to_reddit(subreddit_name):
    reddit = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent=reddit_user_agent,
        username=reddit_username,
        password=reddit_password
    )
    subreddit = reddit.subreddit(subreddit_name)
    subreddit.submit(title, url=link)
    print(f"✅ Posted to r/{subreddit_name}")

# Twitter Posting
def post_to_twitter():
    auth = tweepy.OAuth1UserHandler(
        twitter_api_key, twitter_api_secret,
        twitter_access_token, twitter_access_secret
    )
    api = tweepy.API(auth)
    api.update_status(message)
    print("✅ Posted to Twitter")

# Run the postings
post_to_reddit("migraine")  # Example subreddit
post_to_twitter()
