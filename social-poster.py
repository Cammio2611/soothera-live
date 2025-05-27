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
        subreddit = reddit.subreddit("test")  # ✅ Change to your real target after testing
        subreddit.submit(title, selftext=body)
        print("✅ Reddit post submitted.")
    except Exception as e:
        print(f"❌ Failed to post to Reddit: {e}")

if __name__ == "__main__":
    reddit_title = "Natural Migraine Relief in 2025 — What’s Actually Working for You?"
    reddit_body = (
        "Hey folks, I've been exploring natural ways to manage migraines — especially as more 2025 research is coming out.\n\n"
        "Things like peppermint oil, magnesium, and cold therapy caps keep popping up in blogs and wellness circles.\n\n"
        "I'm curious — has anyone here found success with these remedies? What’s worked (or hasn’t) for you?\n\n"
        "*Just sharing to learn from others — not promoting anything.*"
    )

    post_to_reddit(reddit_title, reddit_body)
