import os
import openai
import random
import uuid
from datetime import datetime

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# List of potential blog topics
topics = [
    "natural remedies for migraines",
    "herbal treatments for anxiety",
    "benefits of aromatherapy",
    "holistic approaches to insomnia",
    "natural ways to boost immunity"
]

# Select a random topic
selected_topic = random.choice(topics)

# Create a dynamic prompt
prompt = f"Write a comprehensive blog post about {selected_topic}, including practical tips and recent research findings."

# Generate the blog content
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1000,
    temperature=0.7
)

blog_content = response.choices[0].text.strip()

# Extract title and meta description
lines = blog_content.split('\n')
title = lines[0] if lines else "Untitled Post"
meta_description = f"{title} - Learn more about {selected_topic} in this comprehensive guide."

# Generate a unique filename
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = f"blog-post-{timestamp}.md"

# Save the blog post
with open(os.path.join("blog", filename), "w", encoding="utf-8") as file:
    file.write(f"# {title}\n\n")
    file.write(blog_content)
    file.write(f"\n\n<!-- Meta Description: {meta_description} -->")
