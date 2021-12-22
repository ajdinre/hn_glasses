import requests
import re

url = 'https://news.ycombinator.com/best'
r = requests.get(url)
html = r.text
urls = set()
for relative_url in re.findall( r'item\?id=[0-9]*', html):
    urls.add('https://news.ycombinator.com/' + relative_url)
print(urls)
