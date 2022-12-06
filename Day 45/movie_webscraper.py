from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

content = response.text

soup = BeautifulSoup(content, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies] #List Comprehension to only get the title
movies = movie_titles[::-1] #This notation to reverse the list

#Write to File
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")






