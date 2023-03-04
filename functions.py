from Vereine import *
import colors as c
import random


'''
@description: reads txt-file and returns a nested list in following form: file = [line1=[], line2=[], ...]
@parameter: filepointer
@return: liste = [zeile1=[], zeile2=[], ...]
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


'''
@description: coloring nodes according to communities
@:parameter:graph, list_communities
@return: color_map[] for use in nx.draw()
'''
def color_nodes(graph, list_communities):
    color_map = []

    for player in graph:
        if player in list_communities[0]:
            color_map.append(c.Blue)
        elif player in list_communities[1]:
            color_map.append(c.SandyBrown)
        elif player in list_communities[2]:
            color_map.append(c.Green)
        elif player in list_communities[3]:
            color_map.append(c.DarkOrange)
        elif player in list_communities[4]:
            color_map.append(c.Red)
        elif player in list_communities[5]:
            color_map.append(c.Purple)
        elif player in list_communities[6]:
            color_map.append(c.Yellow)
        elif player in list_communities[7]:
            color_map.append(c.CornflowerBlue)
        elif player in list_communities[8]:
            color_map.append(c.RosyBrown)
        elif player in list_communities[9]:
            color_map.append(c.Khaki)
        elif player in list_communities[10]:
            color_map.append(c.Coral)
        elif player in list_communities[11]:
            color_map.append(c.OrangeRed)
        elif player in list_communities[12]:
            color_map.append(c.Magenta)
        elif player in list_communities[12]:
            color_map.append(c.Gold)
        elif player in list_communities[13]:
            color_map.append(c.DarkCyan)
        elif player in list_communities[14]:
            color_map.append(c.Peru)
        elif player in list_communities[15]:
            color_map.append(c.ForestGreen)
        elif player in list_communities[16]:
            color_map.append(c.Sienna1)
        elif player in list_communities[17]:
            color_map.append(c.MediumVioletRed)
        elif player in list_communities[18]:
            color_map.append(c.Orchid)
        elif player in list_communities[19]:
            color_map.append(c.LightGoldenrod1)
        elif player in list_communities[20]:
            color_map.append(c.Aquamarine)
        elif player in list_communities[21]:
            color_map.append(c.LimeGreen)
        elif player in list_communities[22]:
            color_map.append(c.LightCoral)
        elif player in list_communities[23]:
            color_map.append(c.Violet)
        elif player in list_communities[24]:
            color_map.append(c.DeepPink)
        elif player in list_communities[25]:
            color_map.append(c.GreenYellow)
        elif player in list_communities[26]:
            color_map.append(c.NavyBlue)
        elif player in list_communities[27]:
            color_map.append(c.tan1)
        elif player in list_communities[28]:
            color_map.append(c.LightSlateGray)
        elif player in list_communities[29]:
            color_map.append(c.Cyan2)
        elif player in list_communities[30]:
            color_map.append(c.MediumSeaGreen)
        elif player in list_communities[31]:
            color_map.append(c.Firebrick3)
        elif player in list_communities[32]:
            color_map.append(c.MediumPurple)

    return color_map


# TODO: write foo() for update positions of nodes according to communities
# aufteilen des Zeichenbereichs in 60*60 Quadrate -> 10 Steps -> Zeichenbereich komplett = 600*600

'''
@description: creates a random list
@parameter: length must be 100 or 101
@return: returns the creates list with random values from 0 to 100 with no duplicates
'''
def unique_random_list(length):
    result = []
    while len(result) < length:
        num = random.randint(0, 100)
        if num not in result:
            result.append(num)
    return result

'''
@description: creates N unique positions-set(x,y)'s in given sector
@parameter: number_positions, sector
@return: returns a list of positions-set()'s
'''
def generate_unique_positions(number_positions, sector):
    positions = set()

    return list(positions)

'''
@description: updates the positions-dict {node1:set(x,y), node2:set(x,y), ...}
@parameter: list_community_nodes
@return: positions_dict -> dictionary with nodes as keys and positions as values, positions as set(x,y)
'''
def update_positions(list_community_nodes):
    positions_dict = {}

    for nodelist in list_community_nodes:
        a=1


    return positions_dict


###sth
###
###

'''
@description:
@parameter:
'''
def generate_positions(num_positions, x_range, y_range):
        """
        Generate num_positions 2D positions within the specified x and y ranges.
        Each position is randomly assigned to a group (integer).
        Returns a list of tuples, where each tuple contains the x and y coordinates
        of a position, as well as its assigned group.
        """
        positions_set = set()  # Set to store unique positions
        while len(positions_set) < num_positions:
            x = random.uniform(x_range[0], x_range[1])
            y = random.uniform(y_range[0], y_range[1])
            #group = random.randint(1, 5)  # Generate a random integer between 1 and 5
            positions_set.add((x, y))  # Add the unique position to set
        return list(positions_set)