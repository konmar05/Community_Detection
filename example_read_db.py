import networkx as nx
import matplotlib.pyplot as plt
from Bundesliga import *
from Vereine import *

fp = open('bundesliga_database.txt', 'r')


def lines_as_lists(filepointer):
    zeilen = filepointer.readlines()
    list_zeilen = []
    # print(zeilen)
    for zeile in zeilen:
        tmp = zeile.rstrip()
        list_zeile = tmp.split('#')

        for i in range(len(list_zeile)):
            if list_zeile[i].isdigit():
                list_zeile[i] = int(list_zeile[i])

        list_zeilen.append(list_zeile)
        # print(list_zeile)
    return list_zeilen


def main():
    plt.figure(figsize=(30, 30))
    bundesliga = {}
    graph_bundesliga = nx.Graph()
    counter = 1

    lines = lines_as_lists(fp)  # getting lines as a list, each line is an own list

    for line in lines:
        bundesliga[line[0]] = Vereine(line)

    for player, clubs in bundesliga.items():
        #print(player, clubs)
        graph_bundesliga.add_node(counter, name=player)
        counter = counter+1
    '''
    for spieler1, vereine1 in bundesliga.items():
        for spieler2, vereine2 in bundesliga.items():

            for jahr, verein in vereine1.vereine.items():
    '''
    knoten = graph_bundesliga.number_of_nodes()
    for i in range(1, knoten+1):
        for j in range(1, knoten+1):

            if (graph_bundesliga._node[i] == graph_bundesliga._node[j]):
                break
            spieler1 = graph_bundesliga._node[i].get('name')
            spieler2 = graph_bundesliga._node[j].get('name')
            vereine1 = bundesliga[spieler1]
            vereine2 = bundesliga[spieler2]
            for jahr1, club1 in vereine1.vereine.items():
                for jahr2, club2 in vereine2.vereine.items():
                    if (jahr1 == jahr2):
                        if (club1 == club2):
                            graph_bundesliga.add_edge(i,j)





    #print(bundesliga)

    nx.draw(graph_bundesliga, with_labels=True, font_weight='normal', pos=nx.spring_layout(graph_bundesliga))
    #plt.figure(1, figsize=(250, 250), dpi=10)
    plt.show()
    #plt.savefig('biggraph.png', dpi=1000)

