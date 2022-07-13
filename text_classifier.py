# text classification of text in various categories of cybercrime activities

from newsapi import NewsApiClient
import pycountry
from dotenv import load_dotenv
import os

load_dotenv()

newsapi = NewsApiClient(api_key=os.getenv('api_key'))
 
# now we will take name of country from user as input
input_country = "India"
input_countries = [f'{input_country.strip()}']
countries = {}
 
# iterate over all the countries in
# the world using pycountry module
for country in pycountry.countries:
 
    # and store the unique code of each country
    # in the dictionary along with it's full name
    countries[country.name] = country.alpha_2
 
# now we will check that the entered country name is
# valid or invalid using the unique code
codes = [countries.get(country.title(), 'Unknown code')
         for country in input_countries]
 
print(f'{codes[0].lower()}')
# now we have to display all the categories from which user will
# decide and enter the name of that category
option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
 
# now we will fetch the new according to the choice of the user
top_headlines = newsapi.get_top_headlines(
 
    # getting top headlines from all the news channels
    q='india', language='en', country=f'{codes[0].lower()}')
 
  # fetch the top news under that category
Headlines = top_headlines['articles']
 
   # now we will display the that news with a good readability for user
if Headlines:
        for articles in Headlines:
            b = articles['title'][::-1].index("-")
            if "news" in (articles['title'][-b+1:]).lower():
                print(
                    f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
            else:
                print(
                    f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
else:
        print(
            f"Sorry no articles found for {input_country}, Something Wrong!!!")
