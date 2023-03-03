import matplotlib.pyplot as plt
import networkx as nx
import functions as f
import colors as c

from networkx.algorithms.community.label_propagation import asyn_lpa_communities


def main():

    plt.figure(figsize=(60, 50))
    fp = open('bundesliga_database_complete.txt', 'r')
    bundesliga = {}
    graph_bundesliga = nx.Graph()

    zeilen = f.read_data(fp)
    f.create_dict_vereine(bundesliga, zeilen)
    f.create_nodes(bundesliga, graph_bundesliga)
    f.add_edges_to_nodes(graph_bundesliga, bundesliga)

    # analysing graph, detecting communities
    ergebnis = asyn_lpa_communities(graph_bundesliga)
    color_map = []
    communities = []

    for community in ergebnis:
        communities.append(community)

    print('Erkannte Communities: ', len(communities))

    # coloring nodes according to communities
    for player in graph_bundesliga:
        if player in communities[0]:
            color_map.append(c.Blue)
        elif player in communities[1]:
            color_map.append(c.SandyBrown)
        elif player in communities[2]:
            color_map.append(c.Green)
        elif player in communities[3]:
            color_map.append(c.DarkOrange)
        elif player in communities[4]:
            color_map.append(c.Red)
        elif player in communities[5]:
            color_map.append(c.Purple)
        elif player in communities[6]:
            color_map.append(c.Yellow)
        elif player in communities[7]:
            color_map.append(c.CornflowerBlue)
        elif player in communities[8]:
            color_map.append(c.RosyBrown)
        elif player in communities[9]:
            color_map.append(c.Khaki)
        elif player in communities[10]:
            color_map.append(c.Coral)
        elif player in communities[11]:
            color_map.append(c.OrangeRed)
        elif player in communities[12]:
            color_map.append(c.Magenta)
        elif player in communities[12]:
            color_map.append(c.Gold)
        elif player in communities[13]:
            color_map.append(c.DarkCyan)
        elif player in communities[14]:
            color_map.append(c.Peru)
        elif player in communities[15]:
            color_map.append(c.ForestGreen)
        elif player in communities[16]:
            color_map.append(c.Sienna1)
        elif player in communities[17]:
            color_map.append(c.MediumVioletRed)
        elif player in communities[18]:
            color_map.append(c.Orchid)
        elif player in communities[19]:
            color_map.append(c.LightGoldenrod1)
        elif player in communities[20]:
            color_map.append(c.Aquamarine)
        elif player in communities[21]:
            color_map.append(c.LimeGreen)
        elif player in communities[22]:
            color_map.append(c.LightCoral)
        elif player in communities[23]:
            color_map.append(c.Violet)
        elif player in communities[24]:
            color_map.append(c.DeepPink)
        elif player in communities[25]:
            color_map.append(c.GreenYellow)
        elif player in communities[26]:
            color_map.append(c.NavyBlue)
        elif player in communities[27]:
            color_map.append(c.tan1)
        elif player in communities[28]:
            color_map.append(c.LightSlateGray)
        elif player in communities[29]:
            color_map.append(c.Cyan2)
        elif player in communities[30]:
            color_map.append(c.MediumSeaGreen)
        elif player in communities[31]:
            color_map.append(c.Firebrick3)
        elif player in communities[32]:
            color_map.append(c.MediumPurple)

    nx.draw(graph_bundesliga, with_labels=True, node_color=color_map, pos=nx.spring_layout(graph_bundesliga))
    plt.show()
