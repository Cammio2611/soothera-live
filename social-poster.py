import os

def post_to_twitter(message):
    twitter_api_key = os.getenv("TWITTER_API_KEY")
    twitter_api_secret = os.getenv("TWITTER_API_SECRET")
    twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    twitter_access_secret = os.getenv("TWITTER_ACCESS_SECRET")

    if not all([twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_secret]):
        print("❌ Missing Twitter credentials.")
        return

    print(f"✅ Would post to Twitter: {message}")
    # TODO: Add real Twitter posting logic here using Tweepy or similar.

def post_to_reddit(title, body):
    reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
    reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    reddit_username = os.getenv("REDDIT_USERNAME")
    reddit_password = os.getenv("REDDIT_PASSWORD")

    if not all([reddit_client_id, reddit_client_secret, reddit_username, reddit_password]):
        print("❌ Missing Reddit credentials.")
        return

    print(f"✅ Would post to Reddit: {title} - {body}")
    # TODO: Add real Reddit posting logic here using PRAW or similar.

if __name__ == "__main__":
    # Example content
    twitter_message = "📝 New migraine relief blog post is live! #migraine #wellness #Soothera"
    reddit_title = "Discover the Latest in Natural Migraine Relief (2025 Edition)"
    reddit_body = "We've published a new article on natural migraine remedies for 2025. Check it out on our website!"

    post_to_twitter(twitter_message)
    post_to_reddit(reddit_title, reddit_body)
