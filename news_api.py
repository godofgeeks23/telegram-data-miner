from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

newsapi = NewsApiClient(api_key=os.getenv('api_key'))

# news_sources = newsapi.get_sources()
# for source in news_sources['sources']:
#     print(source['name'])

# top_headlines = newsapi.get_top_headlines(language='en', country='in')
# for article in top_headlines['articles']:
#     print('Title : ',article['title'])
#     print('Description : ',article['description'],'\n\n')
#     print('Source : ',article['source'])
#     print('URL : ',article['url'])
#     print('Published At : ',article['publishedAt'])
#     print('Author : ',article['author'])
#     print('Content : ',article['content'])

all_articles = newsapi.get_everything(
    q='india AND (riot OR protest OR rally OR election OR festival OR mob OR violence)', language='en')
for article in all_articles['articles']:
    print('Title : ',article['title'])
    print('Description : ',article['description'],'\n\n')
    print('Source : ',article['source']['name'])
    print('URL : ',article['url'])
    print('Published At : ',article['publishedAt'])
    print('Author : ',article['author'])