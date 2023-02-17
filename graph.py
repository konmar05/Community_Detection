import networkx as nx
import matplotlib.pyplot as plt

from networkx.algorithms.community.centrality import girvan_newman

def drawGraph():

    myGraph = nx.Graph()
    myGraph.add_node("neuer", club="fcb", club2="s04", color="red")
    myGraph.add_node("sane", club="fcb", club2="mnc", club3="s04", color="red")
    myGraph.add_node("kimmich", club="fcb", club2="vfb", color="red")
    myGraph.add_node("hummels", club="bvb", club2="fcb", color="yellow")
    myGraph.add_node("schlotterbeck", club="bvb", club2="scf", color="yellow")
    myGraph.add_node("reus", club="bvb", club2="bmg", color="yellow")
    myGraph.add_node("kramer", club="bmg", club2="lev", color="green")
    myGraph.add_node("hofmann", club="bmg", club2="bvb", color="green")
    myGraph.add_node("sommer", club="fcb", club2="bmg", color="red")

    myGraph.add_edge("neuer", "sane", weight=5.0)
    myGraph.add_edge("neuer", "kimmich", weight=5.0)
    myGraph.add_edge("neuer", "sommer", weight=5.0)
    myGraph.add_edge("neuer", "hummels", weight=2.5)
    myGraph.add_edge("hummels", "kimmich", weight=2.5)
    myGraph.add_edge("sane", "kimmich", weight=5.0)
    myGraph.add_edge("sane", "sommer", weight=5.0)
    myGraph.add_edge("sane", "hummels", weight=2.5)
    myGraph.add_edge("hummels", "reus", weight=5.0)
    myGraph.add_edge("hummels", "schlotterbeck", weight=5.0)
    myGraph.add_edge("reus", "schlotterbeck", weight=5.0)
    myGraph.add_edge("reus", "hofmann", weight=2.5)
    myGraph.add_edge("reus", "kramer", weight=2.5)
    myGraph.add_edge("reus", "sommer", weight=2.5)
    myGraph.add_edge("sommer", "hofmann", weight=2.5)
    myGraph.add_edge("sommer", "kramer", weight=2.5)
    myGraph.add_edge("hofmann", "hummels", weight=2.5)
    myGraph.add_edge("hofmann", "schlotterbeck", weight=2.5)

    communities = girvan_newman(myGraph)
    nodeGroups = []

    for c in next(communities):
        nodeGroups.append(list(c))

    print(nodeGroups)
    print(len(nodeGroups))

    colorMap = []

    for node in myGraph:
        if node in nodeGroups[0]:
            colorMap.append("red")
        else:
            colorMap.append("yellow")

    nx.draw(myGraph, node_color=colorMap, with_labels=True)
    plt.show()


