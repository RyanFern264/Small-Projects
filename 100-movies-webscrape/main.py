import requests
from bs4 import BeautifulSoup
from os import remove

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")

titles_scrape = soup.find_all(name="h3", class_="title")

movies = []

for title in titles_scrape:
    movies.append(title.text)


movies.reverse()
print(movies)

remove("movies.txt")
with open("movies.txt", mode="w",encoding="utf-8", newline='') as movie_list:
    for movie in movies:
        movie_list.write(f"{movie}\n")


