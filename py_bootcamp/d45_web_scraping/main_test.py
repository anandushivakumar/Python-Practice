from bs4 import BeautifulSoup
# import lxml if html.parser is not working
import requests


url = "https://news.ycombinator.com/news"
response = requests.get(url)

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

# find all elements with class = "titleline"
all_titles = soup.find_all(class_ = "titleline")
print("The titles are:")
for title in all_titles:
    print(title.text)

# find all article links
all_links = soup.find_all('span', class_="titleline")
print("The links are:")
for span in all_links:
    a = span.find("a") # type: ignore
    if a is not None:
        print(a["href"])  # type: ignore 

# find all article scores
all_scores = soup.find_all(class_ = "score")
print("The scores are:")
for score in all_scores:
    print(score.text)