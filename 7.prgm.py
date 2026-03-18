import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from functools import reduce

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('punkt_tab')

# Initialize Stemmer
stemmer = PorterStemmer()

# -------------------------------
# a) Simple Stemming (List Input)
# -------------------------------
words = ["Consult", "Consultant", "Consulting", "Consultants", "Consultative"]

stemmed_words = [stemmer.stem(word) for word in words]

print("\n--- Simple Stemming ---")
print("Original Words:", words)
print("Stemmed Words:", stemmed_words)

# -----------------------------------------
# b) Stemming using word_tokenize() function
# -----------------------------------------
text = input("\nEnter a sentence: ")

tokens = word_tokenize(text)
stemmed_tokens = [stemmer.stem(word) for word in tokens]

print("\n--- Tokenization + Stemming ---")
print("Original Words:", tokens)
print("Stemmed Words:", stemmed_tokens)

# -----------------------------------------
# c) Stemming using reduce() function
# -----------------------------------------
text2 = input("\nEnter words separated by spaces: ")

tokens2 = word_tokenize(text2)
stemmed_reduce = reduce(lambda acc, word: acc + [stemmer.stem(word)], tokens2, [])

print("\n--- Stemming using reduce() ---")
print("Original Words:", tokens2)
print("Stemmed Words:", stemmed_reduce)