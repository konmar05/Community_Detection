import matplotlib.pyplot as plt
import networkx as nx
import functions as f
import colors as c
import random

from networkx.algorithms.community.label_propagation import asyn_lpa_communities


def main():

    plt.figure(figsize=(60, 50))
    fp = open('bundesliga_database_complete.txt', 'r')
    bundesliga = {}
    positions = {}
    graph_bundesliga = nx.Graph()

    zeilen = f.read_data(fp)
    f.create_dict_vereine(bundesliga, zeilen)
    f.create_nodes(bundesliga, graph_bundesliga)
    f.add_edges_to_nodes(graph_bundesliga, bundesliga)

    # analysing graph, detecting communities
    ergebnis = asyn_lpa_communities(graph_bundesliga)
    communities = []

    for community in ergebnis:
        communities.append(community)

    print('Erkannte Communities: ', len(communities))
    #print(communities)

    color_map = f.color_nodes(graph_bundesliga, communities)

    nx.draw(graph_bundesliga, with_labels=True, node_color=color_map, pos=nx.spring_layout(graph_bundesliga))
    plt.show()
