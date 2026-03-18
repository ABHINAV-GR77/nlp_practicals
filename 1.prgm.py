import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize
sentence = "Hi, My name is Aman, I hope you like my work'."
print(sent_tokenize(sentence))
from nltk.tokenize import TreebankWordTokenizer
word_token = TreebankWordTokenizer()
print(word_token.tokenize(sentence))