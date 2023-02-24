import networkx as nx
import matplotlib.pyplot as plt

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
    # print(print_lines_as_list(fp))

    lines = lines_as_lists(fp)
    first_line = lines[0]
    # first_line.reverse()
    länge = len(first_line)
    länge = int(länge / 3)
    print(länge)

    bundesliga = {}
    info = {}
    vereine = {}

    a = 0
    b = 3
    c = 4
    d = 2

    for i in range(0, länge):

        bundesliga[first_line[a]] = info

        for k in range(first_line[b], first_line[c]):
            info[k] = first_line[d]
        if i == 9:
            break
        b = b + 3
        c = c + 3
        d = d + 3

    print(bundesliga)
    print(info)
    print(vereine)

    '''
    G = nx.Graph()
    nx.draw(G)
    plt.show()
    '''
