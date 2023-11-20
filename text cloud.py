from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import re
import os

if not os.path.exists("img"):
    os.makedirs("img")

def open_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()
    return content

try:
    frase = open_file("C:\\Users\\alexi\\Desktop\\mineria de datos\\Historia.txt")
except UnicodeDecodeError as e:
    print(f"Error al decodificar el archivo: {e}")

frase = open_file("C:\\Users\\alexi\\Desktop\\mineria de datos\\Historia.txt")

words = re.findall(r'\b\w{5,30}\b', frase)

word_counts = Counter(words).most_common(100)  
common_words = [word[0] for word in word_counts]

all_words = " ".join(common_words)

wordcloud = WordCloud(
    background_color="white", min_font_size=20, width=1920, height=1080
).generate(all_words)

img_folder = os.listdir("img")
img_count = len([name for name in img_folder if name.endswith(".png")])

img_name = f"img/word_cloud_{img_count + 1}.png"

plt.figure(figsize=(19.2, 10.8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig(img_name, dpi=300)
plt.show()

