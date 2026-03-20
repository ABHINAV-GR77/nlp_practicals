import nltk
nltk.download('brown')

from nltk.corpus import brown

# Create Conditional Frequency Distribution
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

# Categories (genres)
categories = ['hobbies', 'romance', 'humor']

# Words to check
searchwords = ['may', 'might', 'must', 'will']

# Display result
cfd.tabulate(conditions=categories, samples=searchwords)