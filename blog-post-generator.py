import openai
import os
import datetime
import sys
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ✅ Load API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Predefined fallback topics
default_topics = [
    "Natural Migraine Remedies 2025",
    "The Best Peppermint Oil Uses for Headache Relief",
    "How to Use Cold Therapy for Stress Management",
    "2025 Buyer’s Guide: Migraine Ice Caps",
    "Natural Stress-Relief Products for Better Sleep"
]

# ✅ Get topic from CLI or random fallback
if len(sys.argv) > 1:
    topic = " ".join(sys.argv[1:])
else:
    topic = random.choice(default_topics)

# ✅ Ensure output directories exist
os.makedirs("blog", exist_ok=True)
os.makedirs("scripts", exist_ok=True)

# ✅ Generate blog content
def generate_blog_post(topic):
    prompt = f"Write a 500-word SEO-friendly blog post on '{topic}', including practical tips and a call to action to visit Soothera.com."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Failed to generate blog post: {e}")
        return None

# ✅ Generate YouTube Shorts script
def generate_youtube_script(topic):
    prompt = f"Write a catchy 60-second YouTube Shorts script
