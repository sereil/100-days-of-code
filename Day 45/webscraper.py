from bs4 import BeautifulSoup

import requests


response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
article_links = []
article_titles = []

for article in articles:
    link = article.a.get("href")
    title = article.a.getText()
        
    article_links.append(link)
    article_titles.append(title)
    
# article_tags = article_spans.find("a")
print(article_links)
print(article_titles)
print(article_upvotes)

highest_upvoted_article_id = max(article_upvotes)

idx = article_upvotes.index(highest_upvoted_article_id)

highest_article_link = article_links[idx]
highest_article_title = article_titles[idx]

print(highest_article_link, highest_article_title)

