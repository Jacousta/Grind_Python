from bs4 import BeautifulSoup
with open("website.html") as file:
    data = file.read()
soup = BeautifulSoup(data,"html.parser")
# all_tag = soup.find_all("a")
# for tag in all_tag:
#     print(tag.get("href"))

# heading = soup.find_all(name="h1",id="name")
# print(heading)
h1_heading = soup.select("ul a")
print(h1_heading)