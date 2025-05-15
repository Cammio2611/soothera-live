import subprocess
from datetime import datetime
import os

# Create the output directory if it doesn't exist
output_dir = "videos"
os.makedirs(output_dir, exist_ok=True)

# Generate filename with today's date
today_str = datetime.now().strftime("%Y-%m-%d")
output_file = f"{output_dir}/shorts-{today_str}.mp4"

print(f"🎬 Generating video: {output_file}")

# Example: Generate a 5-second black screen video
cmd = [
    "ffmpeg",
    "-y",  # Overwrite output if exists
    "-f", "lavfi",
    "-i", "color=c=black:s=1280x720:d=5",
    output_file
]

# Show ffmpeg version for debugging
version_check = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
print(version_check.stdout)

# Run the video generation command
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode != 0:
    print("❌ Error generating video:")
    print(result.stderr)
    exit(result.returncode)
else:
    print("✅ Video created successfully!")
    print(f"📂 Saved as: {output_file}")
