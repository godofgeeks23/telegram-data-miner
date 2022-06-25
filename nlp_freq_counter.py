import nltk
from nltk.corpus import stopwords
import re

# # nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# # set([text.parent.name for text in soup.find_all(text=True)])
# text = ''
# with open("txts/msgdump2.txt") as file_in:
#     text = file_in.read()
# text = re.sub(r'\[.*?\]+', '', text)
# text = text.replace('\n', '')
# # print(text)

# tokens = [t for t in text.split()]

# sr = stopwords.words('english')
# clean_tokens = tokens[:]
# for token in tokens:
#     if token in stopwords.words('english'):
#         clean_tokens.remove(token)
# freq = nltk.FreqDist(clean_tokens)

# # for key,val in freq.items():
# # print(str(key) + ':' + str(val))

# freq.plot(20, cumulative=False)



import json
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


stop_words=stopwords.words("english")

wnl=WordNetLemmatizer()

text = ''
with open("txts/msgdump2.txt") as file_in:
    text = file_in.read()

newtext=""
for i in range(len(text)):
    if text[i] in [".","-","_","(",")",",","/","\\",":",";","?","&","•"]:
        newtext+=" "
    else:
        newtext+=text[i]
words=newtext.split()
stemmed=[]
for word in words:
    stemmed.append(wnl.lemmatize(word))
stem_stoped=set()

tags = []

for word in stemmed:
    if word not in stop_words+[''] and word.isalpha() and len(word)>2:
        stem_stoped.add(word)
        tags.append(word)
# print(stem_stoped)

# freq = nltk.FreqDist(tags)
# print(freq)
# freq.plot(50, cumulative=False)

noun_categories = ['NN', 'NNS', 'NNP', 'NNPS']
pos_tagged_tags = nltk.pos_tag(tags)
# print("\npos_tagged_words - ", pos_tagged_tags)
noun_tags = [word for (word, pos) in pos_tagged_tags if(pos[:2] == 'NN' or pos[:2] == 'NNS' or pos[:2] == 'NNP' or pos[:2] == 'NNPS')]
print("\nnouns - ", noun_tags)
freq = nltk.FreqDist(noun_tags)
# print(freq)
freq.plot(50, cumulative=False)


print("----------"*10)