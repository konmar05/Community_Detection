import networkx as nx
import matplotlib.pyplot as plt
import community.community_louvain as cl
import colors
import numpy as np
import functions as f

from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community.label_propagation import asyn_lpa_communities
from networkx.algorithms.community.asyn_fluid import asyn_fluidc

def two():
    # Erstellen eines Graphen
    graph_kclub = nx.karate_club_graph()

    # Ausführen der Community-Detektion
    partition = cl.best_partition(graph_kclub)

    # Definieren der geographischen Koordinaten jedes Knotens basierend auf der Community-Zugehörigkeit
    pos_communities = {}
    for node, community_id in partition.items():
        if community_id not in pos_communities:
            pos_communities[community_id] = {}
        pos_communities[community_id][node] = (community_id, node)

    # Zeichnen des Graphen mit den Koordinaten
    pos = {}
    for community_id, nodes in pos_communities.items():
        subgraph = graph_kclub.subgraph(nodes)
        pos.update(nx.spring_layout(subgraph, k=0.5, center=(community_id, 0)))

    nx.draw(graph_kclub, pos)

    # Anzeigen des Graphen
    plt.show()


def three():

    G = nx.gnm_random_graph(50, 100)

    partition = cl.best_partition(G)

    colors = [plt.get_cmap('tab20')(partition.get(node)) for node in G.nodes()]

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, node_color=colors, with_labels=True, cmap='tab20')
    plt.show()

    for i in range(10):
        # Ändern Sie die Partition
        partition = cl.best_partition(G)

        # Erstellen Sie die Liste der Knotenfarben
        colors = [plt.get_cmap('tab20')(partition.get(node)) for node in G.nodes()]

        # Zeichnen Sie den Graphen mit den Knotenfarben
        plt.subplot(2, 5, i + 1)
        nx.draw_networkx(G, pos=pos, node_color=colors, with_labels=True, cmap='tab20')
        plt.title('Step {}'.format(i + 1))

        # Ändern Sie die Kanten
        G.remove_edges_from(np.random.choice(G.edges(), 10))

    plt.tight_layout()
    plt.show()


def four():
    G = nx.karate_club_graph()
    visit_counts = f.random_walk(G, 0, 100)
    communities = {}
    for node, count in visit_counts.items():
        if count not in communities:
            communities[count] = [node]
        else:
            communities[count].append(node)

    print(communities)
    nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
    plt.show()


