import matplotlib.pyplot as plt
import networkx as nx
import database as db
import graph
from networkx.algorithms.community.centrality import girvan_newman

import requests
from bs4 import BeautifulSoup

def test():
    G = nx.karate_club_graph()
    c = girvan_newman(G)

    node_groups = []
    for com in next(c):
        node_groups.append(list(com))

    print(node_groups)

    color_map = []
    for node in G:
        if node in node_groups[0]:
            color_map.append('blue')
        else:
            color_map.append('green')

    nx.draw(G, node_color=color_map, with_labels=True)
    plt.show()

def main():

    fp = open("database.txt", "a")

    source = "https://www.bundesliga.com"
    count = 0

    links = set()
    result = requests.get("https://www.bundesliga.com/en/bundesliga/player")
    soup = BeautifulSoup(result.content, "html.parser")
    for a in soup.find_all('a', href=True):
        # print("Found the URL:", a['href'])
        if "player" in a['href']:
            links.add(source + a['href'])

    for line in links:
        count = count + 1
        print(line)

    print(count)

    for link in links:
        content = requests.get(link)
        fp.write(link)
        fp.write("\n")
        soup = BeautifulSoup(content.content, "html.parser")
        for bio in soup.find_all("p", class_="vitaparagraph ng-star-inserted"):
            data = bio.text.split("for")
            print(data)
            fp.write(str(data))
            break





# Press the green button to run the script.
if __name__ == '__main__':
    # main()
    # db.getData()
    # graph.drawgraph()
    graph.createnodes()
