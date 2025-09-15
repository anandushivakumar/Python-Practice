import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

# find all movies
movies = soup.find_all(name="h3", class_='title')
movie_list = []
for movie in movies:
    # save into list
    movie_list.append(movie.getText())

final_list = movie_list[::-1]
print(final_list)

# write to file
with open(r"py_bootcamp\d45_web_scraping\movies.txt", "w", encoding="utf-8") as f:
     for movie in final_list:
         f.write(f"{movie}\n")

