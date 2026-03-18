import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

set(stopwords.words('english'))

# sample sentence
text = """He determined to drop his litigation with the monastry, and relinguish his claims to the wood-cuting and 
fishery rihgts at once. He was the more ready to do this becuase the rights had become much less valuable, and he had 
indeed the vaguest idea where the wood and river in question were."""

# set of stop words
stop_words = set(stopwords.words('english'))

# tokens of words
word_tokens = word_tokenize(text)

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print("\n\nOriginal Sentence \n\n")
print(" ".join(word_tokens))

print("\n\nFiltered Sentence \n\n")
print(" ".join(filtered_sentence))