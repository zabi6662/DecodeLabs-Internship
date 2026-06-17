# AI Recommendation Logic - Project 3
# DecodeLabs

from math import sqrt

# Technology database
tech_stacks = {
    "Python Developer": ["python", "data", "automation"],
    "Machine Learning Engineer": ["python", "machine learning", "data"],
    "Web Developer": ["javascript", "html", "css"],
    "Data Scientist": ["python", "data", "statistics"],
    "Mobile App Developer": ["android", "java", "kotlin"],
    "Cyber Security Analyst": ["security", "network", "linux"]
}

# User input
user_input = input(
    "Enter your interests separated by commas: "
).lower().split(",")

user_interests = [item.strip() for item in user_input]

# Cosine similarity
def cosine_similarity(user, tech):
    common = len(set(user) & set(tech))

    if common == 0:
        return 0

    return common / (
        sqrt(len(set(user))) * sqrt(len(set(tech)))
    )

# Calculate scores
scores = {}

for career, skills in tech_stacks.items():
    score = cosine_similarity(user_interests, skills)
    scores[career] = score

# Sort recommendations
recommendations = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("\nRecommended Career Paths:\n")

for career, score in recommendations:
    print(f"{career} --> Similarity Score: {score:.2f}")