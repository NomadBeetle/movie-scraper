import requests
from bs4 import BeautifulSoup

# URL of the archived Empire Online page
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the webpage
response = requests.get(URL)

# Error handling if request fails
if response.status_code != 200:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract movie titles
all_movies = soup.select("h3.title")
movie_titles = [movie.get_text() for movie in all_movies]

# Reverse the list so the #1 movie is on top
movies = movie_titles[::-1]

# Save the movies to a text file
with open("movies.txt", "w", encoding="UTF-8") as file:
    file.write("\n".join(movies))

print("WOOHOO! movies.txt has been created with the top 100 movies!")