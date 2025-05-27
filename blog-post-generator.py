import os
import random
from datetime import datetime
from openai import OpenAI

# Initialize OpenAI client (for SDK >=1.0.0)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ensure blog folder exists
os.makedirs("blog", exist_ok=True)

# Topic pool for variety
topics = [
    "natural remedies for migraines",
    "herbal treatments for anxiety",
    "benefits of aromatherapy",
    "holistic approaches to insomnia",
    "natural ways to boost immunity",
    "essential oils for stress",
    "breathwork for chronic pain",
    "anti-inflammatory diets",
    "peppermint oil vs ice caps",
    "2025 trends in wellness therapy"
]

selected_topic = random.choice(topics)
today = datetime.now().strftime("%Y-%m-%d")

# Generate blog content
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a professional health blog writer."},
        {"role": "user", "content": f"Write a 600-word blog post about {selected_topic}. Include a catchy title and practical tips."}
    ],
    temperature=0.8
)

blog_content = response.choices[0].message.content.strip()

# Extract title and create filename
lines = blog_content.split('\n')
title = lines[0].replace("#", "").strip() if lines else "Untitled Post"
slug = f"{today}-{selected_topic.replace(' ', '-')}"
filename = f"blog/{slug}.md"

# Save blog file
with open(filename, "w", encoding="utf-8") as f:
    f.write(blog_content)

print(f"✅ Blog post generated: {filename}")
