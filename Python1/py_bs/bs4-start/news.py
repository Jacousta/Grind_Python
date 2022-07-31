import requests
from bs4 import BeautifulSoup
arr_heading = []
arr_score = []
arr_points = []
arr_link = []

news = requests.get(url="https://news.ycombinator.com/")
data = news.text
soup = BeautifulSoup(data, "html.parser")
top_heading = soup.find_all("a", class_="titlelink")
score = soup.find_all(name="span", class_="score")

for x in range(len(top_heading)):
    arr_heading.append(top_heading[x].get_text())
    arr_link.append(top_heading[x].get("href"))
    arr_score.append(score[x].get_text())
    arr_points.append(arr_score[x].split()[0])

test_list = list(map(int, arr_points))

high_up = max(test_list)
index = test_list.index(high_up)
print(arr_heading[index], test_list[index] , arr_link[index])
