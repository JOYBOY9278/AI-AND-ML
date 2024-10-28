import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
file = open("y:\\AI and ML\\yashwanth\\nlp.txt")
text = file.read()

nltk.download('punkt')
nltk.download('stopwords')
# Remove stopwords
for word in words:
    if word not in stopwords:
        words_sw_removed.append(word)

stopwords = set(stopwords)
wordcloud = WordCloud(width=800, height=900, background_color='white', stopwords=stopwords,
                      min_font_size=10).generate(text)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# Load image for word cloud mask
cloud = imread("WEEK 11/black-cloud-icon_118813-8126.avif")
wordcloud = WordCloud(width=800, height=900,
                      background_color='white', stopwords=stopwords,
                      min_font_size=10, mask=cloud).generate(text)

plt.figure(figsize=(8, 8), facecolor='None')
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()