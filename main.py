import matplotlib.pyplot as plt
import networkx as nx
import database as db
import example_read_db
import graph
import Bundesliga as b
import Vereine as V

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

def neu():
    player1 = b.Spieler('Spieler')
    player2 = b.Spieler('Markus')
    player3 = b.Spieler('Jordan')

    player1.jahr[2012] = 'Ein Verein'
    player2.jahr[2023] = 'SpVgg Lagerlechfeld'
    player3.jahr[2023] = 'Hertha BSC Berlin'
    player3.jahr[2022] = 'VFL Wolfsburg'

    player1.jahr[1999] = b.Spieler.Vereine()
    player1.jahr[1999] = ['FCB', 'FCA', 'SO4', 'BVB']

    print(player1.name, player1.jahr)
    print(player2.name, player2.jahr)
    print(player3.name, player3.jahr)

    for year, club in player1.jahr.items():

        if type(club) != list:
            print(year, ':', club)
        else:
            for verein in player1.jahr[year]:
                print(year, ':', verein)


# Press the green button to run the script.
if __name__ == '__main__':
    #main()
    #db.getData()
    #graph.drawgraph()
    #graph.createnodes()
    #test()
    example_read_db.main()
    #neu()