import requests
from bs4 import BeautifulSoup as bs
r=requests.get("https://www.kinopoisk.ru/lists/movies/top250/")
html=bs(r.content, "html.parser")

for i in html.select(".items>.base-movie-main-info_mainInfo__ZL_u3"):
    title=i.select(".caption>a")
    print(title[0].text)
