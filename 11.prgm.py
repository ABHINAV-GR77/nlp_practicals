import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

words = word_tokenize(sentence)

tagged_words = pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN>+}"

chunk_parser = RegexpParser(grammar)

chunk_tree = chunk_parser.parse(tagged_words)

noun_phrases = []

for subtree in chunk_tree.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree.leaves())
        noun_phrases.append(phrase)

print("\nExtracted Noun Phrases:")
for np in noun_phrases:
    print(f"- {np}")