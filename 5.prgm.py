import nltk
from nltk.corpus import brown
from pyparsing import conditionAsParseAction

# Ensure required NLTK resources are downloaded
nltk.download('brown')
# Get user input for categories
categories = input("Enter categories (comma-separated): ").split(',')
searchwords = input("Enter search words (comma-separated): ").split(',')
# Remove spaces
categories = [c.strip().lower() for c in categories]
searchwords = [w.strip().lower() for w in searchwords]
# Validate categories
valid_categories = [c for c in categories if c in brown.categories()]
if not valid_categories:
    print("Error: None of the entered categories exist in the Brown corpus.")
    print(f"Available categories: {', '.join(brown.categories())}")
    exit()
# Create Conditional Frequency Distribution
cfd = nltk.ConditionalFreqDist(
    (genre, word.lower())
    for genre in valid_categories
    for word in brown.words(categories=genre)
)
# Display the frequency table
print("\nWord Frequency Table:")
cfd.tabulate(conditionAsParseAction)