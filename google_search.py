# from googlesearch import search

# results = search("apple mac m2", num_results=10, lang="en")

# for result in results:
#     print(result)




from magic_google import MagicGoogle
import pprint

# # Or PROXIES = None
# PROXIES = [{
#     'http': 'http://192.168.2.207:1080',
#     'https': 'http://192.168.2.207:1080'
# }]

# Or MagicGoogle()
mg = MagicGoogle()

#  Crawling the whole page
# result = mg.search_page(query='apple mac m2', num_results=10, lang="en")

# Crawling url
# for url in mg.search_url(query='apple mac m2', num=10):
#     pprint.pprint(u)

for i in mg.search(query="india AND (protest OR riot OR rally OR election)", num=10, language="en"):
    pprint.pprint(i)