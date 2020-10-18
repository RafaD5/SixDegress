from bs4 import BeautifulSoup
import re
import requests


def get_article_links(article):
    url = f"https://en.wikipedia.org{article}"
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')

    body_content = soup.find('div', {'id':'bodyContent'})
    #We just want other wiki articles
    link_pattern = re.compile(r"^(/wiki/)((?!:).)*$")
    html_elements = body_content.find_all('a', {'href':link_pattern})
    links = [element['href'] for element in html_elements]

    return links


def articles_shortest_path(start_articles, target_article):
    global checked_urls
    print(checked_urls)
    
    children_articles = []
    for parent_article in start_articles:
        children_articles += get_article_links(parent_article)
    
    if target_article in children_articles:
        return 'algo'
    else:
        return articles_shortest_path(children_articles, target_article)


start_article = "/wiki/Albert_Einstein"
end_article = "/wiki/Theory_of_relativity"
checked_urls = set()
print(articles_shortest_path(start_article, end_article))