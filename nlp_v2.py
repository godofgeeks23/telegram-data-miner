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

filtered_list = ([re.sub('[^a-zA-Z0-9]+', '', _) for _ in filtered_list])
filtered_list = [element for element in filtered_list if any(digit not in element for digit in "1234567890")]
filtered_list = [x for x in filtered_list if not any(x1.isdigit() for x1 in x)]
filtered_list = list(filter(None, filtered_list))
filtered_list = [x for x in filtered_list if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
filtered_list = [x for x in words if len(x) > 2]
filtered_list = [x for x in filtered_list if x.isalpha()]
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