import networkx as nx
import matplotlib.pyplot as plt
from Bundesliga import *
from Vereine import *

fp = open('test_database.txt', 'r')


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

    bundesliga = {}
    graph_bundesliga = nx.Graph()
    counter = 1

    lines = lines_as_lists(fp)  # getting lines as a list, each line is an own list

    for line in lines:
        bundesliga[line[0]] = Vereine(line)

    for player, clubs in bundesliga.items():
        print(player, clubs)
        graph_bundesliga.add_node(counter, name=player)
        counter = counter+1

    nx.draw(graph_bundesliga, with_labels=True, pos=nx.spring_layout(graph_bundesliga))
    plt.show()

