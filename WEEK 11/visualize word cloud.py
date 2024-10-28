import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS

file = open("y:\\AI and ML\\yashwanth\\nlp.txt")
text = file.read()

stopword=set(STOPWORDS)

wordcloud=WordCloud(width=800,height=900,
                    background_color='white',
                    stopwords=stopword,
                    min_font_size=10).generate(text)
plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()


from skimage.io import imread
cloud=imread("Y:/AI and ML/PY WEEKS/WEEK 11/images/img.jpg")
plt.imshow(cloud)

stopword=set(STOPWORDS)

wordcloud=WordCloud(width=800,height=900,
                    background_color='white',
                    stopwords=stopword,
                    min_font_size=10,mask=cloud).generate(text)
plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
