from Vereine import *


'''
@description: reads txt-file and returns a nested list in following form: file = [line1=[], line2=[], ...]
@parameter: filepointer
'''


def read_data(filepointer):
    zeilen = filepointer.readlines()
    list_zeilen = []

    for zeile in zeilen:
        tmp = zeile.rstrip()
        list_zeile = tmp.split('#')

        for i in range(len(list_zeile)):
            if list_zeile[i].isdigit():
                list_zeile[i] = int(list_zeile[i])

        list_zeilen.append(list_zeile)

    return list_zeilen


'''
@description: creates and adds a new dictionary = {year:'club'} for each player in given league-dictionary 
@:parameter: dictionary, list
'''


def create_dict_vereine(dict_to_write, list_to_read):
    for line in list_to_read:
        dict_to_write[line[0]] = Vereine(line)


'''
@description: iterates trough dictionary and adds every key:value pair to the graph
@parameter: dictionary, graph
'''


def create_nodes(dictionary, graph):
    id_for_node = 1
    for player, clubs in dictionary.items():
        graph.add_node(id_for_node, name=player)
        id_for_node = id_for_node+1


'''
@description: add edges to the nodes from players how played in the same year in the same club
@parameter: graph, dictionary from which the graph was created
'''


def add_edges_to_nodes(graph, dictionary):
    knoten = graph.number_of_nodes()
    for i in range(1, knoten+1):
        for j in range(1, knoten+1):

            if (graph._node[i] == graph._node[j]):
                break
            spieler1 = graph._node[i].get('name')
            spieler2 = graph._node[j].get('name')
            vereine1 = dictionary[spieler1]
            vereine2 = dictionary[spieler2]
            for jahr1, club1 in vereine1.vereine.items():
                for jahr2, club2 in vereine2.vereine.items():
                    if (jahr1 == jahr2):
                        if (club1 == club2):
                            if (graph.has_edge(i, j)):
                                break
                            else:
                                graph.add_edge(i, j)
