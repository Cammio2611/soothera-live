import datetime

# Example post topics
topics = [
    "Natural Migraine Relief Tips",
    "Best Migraine Ice Caps for 2025",
    "How Essential Oils Can Help Headaches",
    "Foods to Avoid if You Suffer Migraines"
]

# Format for Twitter and Pinterest
today = datetime.date.today().strftime("%B %d, %Y")

for topic in topics:
    tweet = f"{topic} - Find out more at Soothera.com #MigraineRelief #WellnessTips #{today.replace(' ', '')}"
    pinterest_description = f"Discover {topic.lower()} on Soothera.com. Learn natural remedies, product tips, and more. #MigraineRelief #Wellness"

    print("\n---")
    print("📢 Twitter Post:")
    print(tweet)
    print("\n📌 Pinterest Description:")
    print(pinterest_description)
    print("---")
