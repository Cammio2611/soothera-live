import os
import openai
import glob

openai.api_key = os.getenv("OPENAI_API_KEY")

BLOG_DIR = "blog"
SHORTS_DIR = "shorts"
os.makedirs(SHORTS_DIR, exist_ok=True)

def get_latest_blog_post():
    files = sorted(glob.glob(f"{BLOG_DIR}/*.md"), reverse=True)
    if not files:
        raise FileNotFoundError("❌ No blog posts found.")
    filepath = files[0]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    slug = os.path.basename(filepath).replace(".md", "")
    return content, slug

def generate_youtube_script(blog_content):
    messages = [
        {"role": "system", "content": "You are a scriptwriter for YouTube Shorts."},
        {"role": "user", "content": f"Turn this blog post into a 60-second YouTube Shorts script with visual scene suggestions:\n\n{blog_content}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    blog_text, slug = get_latest_blog_post()
    script = generate_youtube_script(blog_text)

    output_path = os.path.join(SHORTS_DIR, f"{slug}-short.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(script)

    print(f"✅ YouTube Shorts script generated: {output_path}")
