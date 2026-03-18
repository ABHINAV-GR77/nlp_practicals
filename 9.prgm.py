import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    print("\nOriginal | POS Tag | Lemmatized")
    print("-" * 40)

    for word, tag in tagged_words:
        pos = get_wordnet_pos(tag)
        print(f"{word:10} | {tag:7} | {lemmatizer.lemmatize(word, pos)}")

sentence = input("Enter a sentence: ")
lemmatize_sentence(sentence)