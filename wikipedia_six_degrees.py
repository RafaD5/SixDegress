from bs4 import BeautifulSoup
import re
import requests

#Project modules
from node import Node


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


def articles_shortest_path(start_article, target_article, max_generations=3):
    counter = 0
    head_node = Node(start_article, None)
    final_node = Node(target_article, None)
    article_links = get_article_links(start_article)
    next_generation = [Node(child, head_node) for child in article_links]
    while counter < max_generations:
        if final_node in next_generation:
            # Get the article. Ask for parents.
            final_node_pos = next_generation.index(final_node)
            final_node = next_generation[final_node_pos]
            path = [final_node.article]
            while final_node.parent is not None:
                final_node = final_node.parent
                path.append(final_node.article)
            return path
        else:
            current_generation = next_generation
            next_generation = []
            for temporal_node in current_generation:
                print(temporal_node.article)
                article_links = get_article_links(temporal_node.article)
                child_nodes = ([Node(child, temporal_node) 
                                for child in article_links])
                next_generation += child_nodes
        counter += 1

    return False


start_article = "/wiki/Indigenous_peoples_in_Colombia"
end_article = "/wiki/Maya_civilization"
print(articles_shortest_path(start_article, end_article))