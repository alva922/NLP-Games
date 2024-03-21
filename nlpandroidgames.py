import os
os.chdir('YOURPATH')    # Set working directory
os. getcwd() 
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
df = pd.read_csv("android-games.csv")
df.isna().sum()
text = " ".join(cat.split()[1] for cat in df.category)
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
#plt.show()
plt.savefig("wordcloudtextgames.png")
#Creating the text variable

text2 = " ".join(title for title in df.title)

# Creating word_cloud with text as argument in .generate() method

word_cloud2 = WordCloud(collocations = False, background_color = 'white').generate(text2)

# Display the generated Word Cloud

plt.imshow(word_cloud2, interpolation='bilinear')

plt.axis("off")

#plt.show()
plt.savefig("wordcloudtitlesgames.png")
