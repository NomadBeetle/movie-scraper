# Top 100 Movies Scraper

This is a simple Python script that scrapes the **Top 100 Movies** list from an archived version of Empire Online's website. It uses `requests` and `BeautifulSoup` to fetch and parse the data, then saves the movies into a `movies.txt` file.

I decided to push this project to GitHub because it's my **first ever web scraping project**. 

## Features
- Fetches the top 100 movies from the archived page.
- Parses movie titles cleanly using BeautifulSoup.
- Outputs the results in a neatly formatted text file.
- Simple and beginner friendly code.

## Tech Stack
- **Python 3**
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/top-100-movies-scraper.git
   ```
2. Navigate to the project folder:
   ```bash
   cd top-100-movies-scraper
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the scraper:
   ```bash
   python scraper.py
   ```

After running, you will find a file named **movies.txt** containing the top 100 movies.

## Example Output (movies.txt)
```
The Shawshank Redemption
The Godfather
The Dark Knight
...
```

## Why I Made This
This is my **first step into web scraping**, and I wanted to try out some basic techniques and save the results to a file. I thought it would be fun to share it here on GitHub as a record of my learning journey.

---

## Author

**Azaan (NomadBeetle)**
[GitHub](https://github.com/NomadBeetle) • [LinkedIn](https://linkedin.com/in/nomadbeetle)