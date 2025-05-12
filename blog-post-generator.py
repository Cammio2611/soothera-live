import openai
import datetime

# 🔑 Insert your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your target keyword or topic
topic = "Natural Migraine Remedies 2025"

# Generate blog content using GPT-3.5
def generate_blog_post(topic):
    prompt = f"Write a 500-word SEO-friendly blog post on '{topic}', including practical tips and a call to action to visit Soothera.com."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Generate content
blog_content = generate_blog_post(topic)

# Generate filename with date
today = datetime.date.today().strftime("%Y-%m-%d")
filename = f"blog-post-{today}.md"

# Save to file
with open(filename, "w", encoding="utf-8") as file:
    file.write(blog_content)

print(f"✅ Blog post saved as {filename}")