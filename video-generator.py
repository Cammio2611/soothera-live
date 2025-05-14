import os
import datetime
import subprocess

# Directories
scripts_dir = "scripts"
videos_dir = "videos"
os.makedirs(videos_dir, exist_ok=True)

# Get latest script
script_files = sorted(
    [f for f in os.listdir(scripts_dir) if f.endswith(".txt")],
    reverse=True
)

if not script_files:
    print("❌ No scripts found in 'scripts/' directory.")
    exit(1)

latest_script_path = os.path.join(scripts_dir, script_files[0])

# Read script content
with open(latest_script_path, "r", encoding="utf-8") as file:
    script_content = file.read()

# Generate overlay text file for ffmpeg
overlay_text_file = "overlay.txt"
with open(overlay_text_file, "w", encoding="utf-8") as file:
    file.write(script_content)

# Output video filename
today = datetime.date.today().strftime("%Y-%m-%d")
video_filename = os.path.join(videos_dir, f"shorts-{today}.mp4")

# FFmpeg Command Example (Static Image with Text Overlay)
# Make sure 'background.jpg' exists in your project folder
cmd = [
    "ffmpeg",
    "-loop", "1",
    "-i", "background.jpg",
    "-f", "lavfi",
    "-i", "anullsrc",
    "-t", "60",
    "-vf", f"drawtext=textfile={overlay_text_file}:fontcolor=white:fontsize=24:x=(w-text_w)/2:y=(h-text_h)/2",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-shortest",
    video_filename
]

# Run FFmpeg
print(f"🎬 Generating video: {video_filename}")
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result.returncode == 0:
    print(f"✅ Video generated successfully at {video_filename}")
else:
    print(f"❌ Video generation failed:\n{result.stderr.decode()}")
