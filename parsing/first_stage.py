from bs4 import BeautifulSoup

with open("parsing/index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

search_class = soup.find_all(class_="item-grid-info")

links = []

for item in search_class:
    a_tag = item.find("a")
    links.append(a_tag["href"])