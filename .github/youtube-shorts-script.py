import random

# Example migraine tips for short videos
tips = [
    "Use a cold compress on your forehead for 15 minutes to numb the pain.",
    "Apply peppermint oil to your temples and neck for natural relief.",
    "Practice deep breathing for 5 minutes to relax your body and mind.",
    "Avoid bright screens and take a break in a dark, quiet room.",
    "Stay hydrated! Dehydration is a common migraine trigger."
]

# Randomly select a tip
selected_tip = random.choice(tips)

# Format as YouTube Shorts script
script = f"""
🎥 Soothera Migraine Tip of the Day 🎥

Hey Soothera family! 👋 Struggling with migraines? Here’s a quick tip:

{selected_tip}

Try it today and let us know if it helps!  
For more tips, visit Soothera.com 💆‍♀️💆‍♂️

#MigraineRelief #Soothera #WellnessTips #Shorts
"""

# Print script for use
print(script)
