import requests
from bs4 import BeautifulSoup

arr_movie = []

movies = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = movies.text
soup = BeautifulSoup(data, "html.parser")
name = soup.find_all(name="h3", class_="title")
for x in range(len(name)):
    arr_movie.append(name[x].get_text())
ol_movie = arr_movie[::-1]
with open("movies.txt", mode="w") as file:
    for movie in ol_movie:
        file.write(f"{movie} \n")
