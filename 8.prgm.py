import snowballstemmer

# List of supported languages
supported_languages = [
    'arabic', 'armenian', 'basque', 'brazilian', 'bulgarian', 'catalan',
    'czech', 'danish', 'dutch', 'english', 'finnish', 'french', 'german',
    'hungarian', 'italian', 'latvian', 'norwegian', 'porter', 'portuguese',
    'romanian', 'russian', 'spanish', 'swedish', 'turkish'
]
print("Supported Languages:")
for lang in supported_languages:
    print("-", lang)
language = input("\nEnter language: ").strip().lower()
if language not in supported_languages:
    print("Invalid language!")
else:
    stemmer = snowballstemmer.stemmer(language)
    text = input("Enter text to stem: ").strip()
    words = text.split()
    stemmed_words = stemmer.stemWords(words)
    print("\nOriginal Words:", words)
    print("Stemmed Words:", stemmed_words)