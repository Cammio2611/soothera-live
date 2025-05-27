import os
import praw

def post_to_reddit(title, body):
    reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
    reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    reddit_username = os.getenv("REDDIT_USERNAME")
    reddit_password = os.getenv("REDDIT_PASSWORD")

    if not all([reddit_client_id, reddit_client_secret, reddit_username, reddit_password]):
        print("❌ Missing Reddit credentials.")
        return

    try:
        reddit = praw.Reddit(
            client_id=reddit_client_id,
            client_secret=reddit_client_secret,
            user_agent=f"SootheraBot/0.1 by {reddit_username}",
            username=reddit_username,
            password=reddit_password
        )
        subreddit = reddit.subreddit("test")  # 🔁 Change this to your actual target subreddit
        subreddit.submit(title, selftext=body)
        print("✅ Reddit post submitted.")
    except Exception as e:
        print(f"❌ Failed to post to Reddit: {e}")

if __name__ == "__main__":
    # Replace with dynamic values later if needed
    reddit_title = "Discover the Latest in Natural Migraine Relief (2025 Edition)"
    reddit_body = "We've published a new article on natural migraine remedies for 2025. Check it out on our website!"

    post_to_reddit(reddit_title, reddit_body)
