import json
import os
from datetime import datetime

BLOG_DIR = "blog"
INDEX_FILE = "blog-index.json"

def get_latest_blog():
    files = sorted([f for f in os.listdir(BLOG_DIR) if f.endswith(".md")], reverse=True)
    if not files:
        return None
    filename = files[0]
    slug = filename.replace(".md", "")
    path = os.path.join(BLOG_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    title = lines[0].replace("#", "").strip() if lines else slug
    return {
        "slug": slug,
        "title": title,
        "description": f"New post about {slug.replace('-', ' ')}.",
        "date": datetime.now().strftime("%Y-%m-%d")
    }

def update_blog_index():
    post = get_latest_blog()
    if not post:
        print("❌ No blog post found.")
        return

    # Load or create index file
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index = json.load(f)
    else:
        index = []

    # Avoid duplicates
    if any(item["slug"] == post["slug"] for item in index):
        print("ℹ️ Blog post already in index.")
        return

    index.insert(0, post)  # Insert newest first
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print(f"✅ blog-index.json updated with: {post['slug']}")

if __name__ == "__main__":
    update_blog_index()
