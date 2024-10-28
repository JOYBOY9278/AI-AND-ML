import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS

nltk.download('punkt')
nltk.download('stopwords')


# Load the text file
file = open("y:\\AI and ML\\yashwanth\\nlp.txt")
text = file.read()

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Tokenize sentences
sentences = sent_tokenize(text)
print("Number of sentences:", len(sentences))

for i in range(len(sentences)): 
    print("\nSentence", i + 1, ":\n", sentences[i])

# Tokenize words
words = word_tokenize(text)
print("Total number of words:", len(words))
print(words)

# Frequency distribution of words
all_fdist = FreqDist(words)
print(all_fdist['service'])

# Plotting frequency distribution
all_fdist = pd.Series(dict(all_fdist))
fig, ax = plt.subplots(figsize=(10, 10))
all_fdist.plot(kind='bar')
plt.title("Frequency Distribution of Words")
plt.ylabel("Counts")

# Preprocess text
text = text.lower()
text = re.sub('[^A-Za-z0-9]+', ' ', text)
text = re.sub(r"\S*\d\S*", "", text).strip()

# Tokenize words again after preprocessing
words = word_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')
words_sw_removed = []

# Remove stopwords
for word in words:
    if word not in stopwords:
        words_sw_removed.append(word)

# Update frequency distribution
all_fdist = all_fdist.add(FreqDist(words_sw_removed))
all_fdist = pd.Series(dict(all_fdist))
fig, ax = plt.subplots(figsize=(7, 7))

# Plotting frequency distribution after stopword removal
all_fdist.plot(kind='bar')
plt.title("Frequency Distribution of Words After Stopword Removal")
plt.ylabel("Count")


