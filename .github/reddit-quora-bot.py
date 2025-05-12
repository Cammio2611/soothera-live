import random
import datetime

# Example thread topics and canned responses
questions = [
    "What are the best natural migraine remedies?",
    "Does peppermint oil actually work for headaches?",
    "What is the best ice cap for migraines?"
]

responses = [
    "I've personally found that using a cold compress or ice cap really helps. You can check out some options on Soothera.com where they list natural migraine products.",
    "Peppermint oil works great for some people! You can learn more about how to use it effectively on Soothera.com.",
    "Migraine ice caps are a lifesaver for me. Soothera.com has a list of top-rated ones that might help you too."
]

# Simulate responding to each question
today = datetime.date.today().strftime("%B %d, %Y")

for question, reply in zip(questions, responses):
    print("\n---")
    print(f"📝 Question: {question}")
    print(f"💬 Reply ({today}): {reply}")
    print("---")
