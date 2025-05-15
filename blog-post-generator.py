import openai
import os

# Load API Key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def generate_blog_post(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a blog writing assistant."},
                {"role": "user", "content": f"Write a detailed blog post about {topic}."}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error generating blog post: {e}")
        return None

if __name__ == "__main__":
    topic = "Natural Migraine Remedies 2025"
    content = generate_blog_post(topic)
    
    if content:
        print("✅ Blog Post Generated Successfully:\n")
        print(content)
    else:
        print("⚠️ No content generated.")
