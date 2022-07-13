from newspaper import Article
import nltk

url = "https://www.timesnownews.com/india/kanpur-violence-stone-pelters-were-paid-rs-500-1000-rioters-who-used-petrol-bombs-received-rs-5000-article-92848618"
 

article = Article(url, language="en")

article.download()
article.parse()
nltk.download('punkt')
article.nlp()

print("Article's Title:")
print(article.title)
print()

print(f"Published Date: {article.publish_date}")
print()

print(f"Authors:{article.authors}")
print()

print("Article's Text:")
print(article.text)
print()

print("Article's Summary:")
print(article.summary)
print()

print("Article's Keywords:")
print(article.keywords)