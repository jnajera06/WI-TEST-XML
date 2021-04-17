# pip install requests

import lxml.html
import requests

url =  "https://www.imdb.com/calendar/?ref_=nv_mv_cal"
response = requests.get(url, stream=True)
response.raw.decode_content = True
tree = lxml.html.parse(response.raw)

for i in tree.xpath('//div[@id="main"]/h4/following-sibling::ul[1]/li/a/text()'):
    print(i)


# import requests
# from bs4 import BeautifulSoup


# vgm_url = 'https://www.imdb.com/calendar/?ref_=nv_mv_cal'
# html_text = requests.get(vgm_url).text
# soup = BeautifulSoup(html_text, 'html.parser')

# for link in soup.find_all('a'):
#     print(link.get('href'))