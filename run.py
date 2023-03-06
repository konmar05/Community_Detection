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
    graph_bundesliga_complete = nx.Graph()

    zeilen = f.read_data(fp)
    f.create_dict_vereine(bundesliga, zeilen)
    f.create_nodes(bundesliga, graph_bundesliga_complete)
    f.add_edges_to_nodes(graph_bundesliga_complete, bundesliga)

    # analysing graph, detecting communities
    ergebnis = asyn_lpa_communities(graph_bundesliga_complete)

    ergebnis_random_walk = f.random_walk(graph_bundesliga_complete, 50, 3000)
    print('Random Walk: ', len(ergebnis_random_walk))

    communities = []

    for community in ergebnis:
        communities.append(community)

    print('Erkannte Communities: ', len(communities))

    '''
    for com in communities:
        graph_bundesliga_complete.add_nodes_from(com)
    for com in communities:
        subgraph = nx.complete_graph(com)
        graph_bundesliga_complete.add_edges_from(subgraph.edges())

    pos = nx.spring_layout(graph_bundesliga_complete)

    for i, comu in enumerate(communities):
        nx.draw_networkx_nodes(graph_bundesliga_complete, pos, nodelist=comu, node_color=f'C{i}', label=f'Community {i+1}')

    nx.draw_networkx_edges(graph_bundesliga_complete, pos, edge_color='grey')
    plt.legend()
    plt.show()

    
    pos_test = f.update_positions(communities)
    #print(communities)

    color_map = f.color_nodes(graph_bundesliga_complete, communities)

    #nx.draw(graph_bundesliga_complete, with_labels=True, node_color=color_map, pos=nx.spring_layout(graph_bundesliga_complete))
    nx.draw(graph_bundesliga_complete, with_labels=True, node_color=color_map, pos=pos_test)

    plt.show()
    '''


def main2():
    graph_bundesliga_small = f.bundesliga_small()

    # test if random walk algorithm is working fine
    communities_detected = f.random_walk(graph_bundesliga_small, 1, 70)
    print(communities_detected)
    print(len(communities_detected))
    nx.draw(graph_bundesliga_small, pos=nx.spring_layout(graph_bundesliga_small), with_labels=True)
    plt.show()
