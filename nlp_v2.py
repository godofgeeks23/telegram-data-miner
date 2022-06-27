from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
import nltk
from nltk.stem import WordNetLemmatizer
import re

# nltk.download('punkt')

text = ''
with open("txts/msgdump2.txt") as file_in:
    text = file_in.read()

words = word_tokenize(text)
# print("\nwords - ", words)

stop_words = set(stopwords.words("english"))
filtered_list = []
for word in words:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
try:
    while True:
        filtered_list.remove('.')
        filtered_list.remove(',')
        filtered_list.remove("'s")
except ValueError:
    pass

filtered_list = ([re.sub('[^a-zA-Z0-9]+', '', _) for _ in filtered_list])
filtered_list = list(filter(None, filtered_list))
filtered_list = [x for x in filtered_list if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
print("\nfiltered_list - ", filtered_list)


# stemmer = PorterStemmer()
stemmer = SnowballStemmer("english")
stemmed_words = [stemmer.stem(word) for word in filtered_list]
# print("\nstemmed_words - ", stemmed_words)

pos_tagged_words = nltk.pos_tag(filtered_list)
# print("\npos_tagged_words - ", pos_tagged_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_list]
# print("\nlemmatized_words - ", lemmatized_words)

freq = nltk.FreqDist(lemmatized_words)
# print(freq)
freq.plot(100, cumulative=False)