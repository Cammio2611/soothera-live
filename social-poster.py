import os
import praw

# Load credentials from environment
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_username = os.getenv("REDDIT_USERNAME")
reddit_password = os.getenv("REDDIT_PASSWORD")

def post_to_reddit(title, body, subreddit_name="test"):
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

        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title=title, selftext=body)
        print(f"✅ Reddit post submitted to r/{subreddit_name}: {submission.shortlink}")

    except Exception as e:
        print(f"❌ Failed to post to Reddit: {e}")

if __name__ == "__main__":
    # Friendly discussion prompt based on latest blog topic
    title = "Natural Migraine Relief in 2025 — What’s Actually Working for You?"
    body = (
        "Hey folks, I’ve been exploring natural migraine relief options lately. "
        "Things like peppermint oil, magnesium, and cold therapy caps keep coming up in new research and articles.\n\n"
        "Just wondering — has anyone here tried these? Did they help? Or is it just placebo?\n\n"
        "*Not selling anything, just curious to hear from others in the community.*"
    )

    # Recommended: use "test" for now; switch to target subreddit later
    post_to_reddit(title, body, subreddit_name="test")
