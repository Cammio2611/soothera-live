import os
import subprocess
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_youtube_script(topic):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional video script writer."},
                {"role": "user", "content": f"Write a short YouTube script about {topic}."}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ Error generating YouTube script: {e}")
        return None

def generate_video(script_text, output_path):
    try:
        print(f"🎬 Generating video: {output_path}")
        with open("script.txt", "w") as f:
            f.write(script_text)

        cmd = ["ffmpeg", "-f", "lavfi", "-i", "color=c=black:s=1280x720:d=5",
               "-vf", "drawtext=text='Soothera Shorts':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2",
               "-y", output_path]
        
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("✅ Video generated successfully.")
        else:
            print(f"❌ ffmpeg error:\n{result.stderr.decode()}")
    except Exception as e:
        print(f"❌ Video generation failed: {e}")

if __name__ == "__main__":
    topic = "Natural Migraine Remedies 2025"
    script = generate_youtube_script(topic)

    if script:
        print("✅ YouTube Script Generated Successfully:\n")
        print(script)
        generate_video(script, f"videos/shorts-{topic.replace(' ', '-').lower()}.mp4")
    else:
        print("⚠️ No content generated.")
