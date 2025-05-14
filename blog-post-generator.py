import openai
import os
import datetime

# ✅ Load API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Define target topic (you could expand this to accept CLI arguments)
topic = "Natural Migraine Remedies 2025"

# ✅ Ensure the blog directory exists
output_dir = "blog"
os.makedirs(output_dir, exist_ok=True)

# ✅ Generate blog content using GPT-3.5
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

# ✅ Generate content
blog_content = generate_blog_post(topic)

# ✅ Save to /blog/ directory if content was generated
if blog_content:
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = os.path.join(output_dir, f"blog-post-{today}.md")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(blog_content)
    print(f"✅ Blog post saved as {filename}")
else:
    print("⚠️ No content generated.")
