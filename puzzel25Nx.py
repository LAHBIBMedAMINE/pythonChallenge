import networkx as nx


def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for line in file:
            mylist.append(line.strip())
    return mylist


def tableData(rawFile):
    listofvectors = []
    for line in rawFile:
        vector = []
        lineSplited = line.strip().split(':')
        vector.append(lineSplited[0].strip())
        for cnx in lineSplited[1].strip().split(" "):
            vector.append(cnx)
        listofvectors.append(vector)

    return listofvectors


testPathfile = "puzzel25Test.txt"
puzzlechallengefile = "puzzle25challenge.txt"
#listofconnection = tableData(textTolist(testPathfile))
listofconnection = tableData(textTolist(puzzlechallengefile))


# [print(item) for item in listofconnection]

def dicOfCnx(listofconnection):
    setofNode = set()
    for item in listofconnection:
        for node in item:
            setofNode.add(node)

    dicOfNodeCnx = {key: set() for key in setofNode}  # i create a dictionary for cnx of each node

    for item in listofconnection:
        for node in item:
            if (node != item[0]):
                dicOfNodeCnx[item[0]].add(node)
                dicOfNodeCnx[node].add(item[0])

    return dicOfNodeCnx


mydicOfNodeCnx = dicOfCnx(listofconnection)

g = nx.Graph()

for node , cnx in mydicOfNodeCnx.items():
    for c in cnx:
        g.add_edge(node,c)
        g.add_edge(c, node)

print(g)
print(nx.minimum_edge_cut(g))
g.remove_edges_from(nx.minimum_edge_cut(g))

groupA,groupB =nx.connected_components(g)
print(len(groupA),len(groupB), len(groupA)*len(groupB))