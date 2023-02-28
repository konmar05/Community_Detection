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

    print(lines[0])
    for i in range(0, len(first_line)):
        print(i, ' : ', first_line[i])

    length = int(len(first_line) / 3)

    bundesliga = {}
    info = {}
    vereine = set()

    name = 0
    akt_verein = 1
    vereinsname = 2
    von = 3
    bis = 4


    for i in range(0, length):
        bundesliga[first_line[name]] = info
        if (first_line[von] == first_line[bis]):
            info[first_line[von]] = first_line[vereinsname]
        else:
            for k in range(first_line[von], first_line[bis]):
                info[k] = first_line[vereinsname]

        vereinsname = vereinsname+3
        von = von+3
        bis = bis+3
        if (bis >= len(first_line)):
            for index in range(first_line[von], 2023):
                info[index] = first_line[vereinsname]
            info[2023] = first_line[akt_verein]
            break

    print(bundesliga)
    #print(info)
    #print(vereine)

    '''
    G = nx.Graph()
    nx.draw(G)
    plt.show()
    '''
