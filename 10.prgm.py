import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)

tagged_words = pos_tag(words)

print("\nOriginal | POS Tag")
print("-" * 30)

for word, tag in tagged_words:
    print(f"{word:10} | {tag}")