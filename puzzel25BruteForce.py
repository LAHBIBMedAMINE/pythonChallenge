from itertools import combinations
import copy


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
# listofconnection = tableData(textTolist(testPathfile))
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


# for key, value in dicOfNodeCnx.items():
# print(f"{key}: {value}")

def groupsCnx(dicOfNodeCnx):
    def groupConstruct(dicOfNodeCnx, Node):
        group = dicOfNodeCnx[Node]
        lenghtBeforeMerge = len(group)
        lenghtafterMerge = 0
        while (lenghtBeforeMerge != lenghtafterMerge):
            lenghtBeforeMerge = len(group)
            for node in group:
                group = group.union(dicOfNodeCnx[node])
            lenghtafterMerge = len(group)
        return group

    longest_set_key = max(dicOfNodeCnx, key=lambda k: len(dicOfNodeCnx[k]))
    group0 = groupConstruct(dicOfNodeCnx, longest_set_key)
    # group0 = groupConstruct(dicOfNodeCnx, list(dicOfNodeCnx.keys())[0])
    groups = []
    groups.append(group0)

    sum_of_lengths = sum(len(s) for s in groups)
    while sum_of_lengths < len(dicOfNodeCnx.keys()):
        diffentNode = set(dicOfNodeCnx.keys()).difference(set().union(*groups))
        groups.append(groupConstruct(dicOfNodeCnx, list(diffentNode)[0]))
        sum_of_lengths = sum(len(s) for s in groups)

    numberofgroups = len(groups)
    lengths = [len(sublist) for sublist in groups]

    return numberofgroups, lengths


# print(groupsCnx(dicOfNodeCnx),len(groupsCnx(dicOfNodeCnx)))
# print(set(dicOfNodeCnx.keys()),len(dicOfNodeCnx.keys()))


all_pairs = list(combinations(mydicOfNodeCnx.keys(), 2))  # brute force will take a night
# all_pairs = [('mnl', 'nmz'), ('txm', 'fdb'), ('jpn', 'vgf')] # this is the solution 785 766 601310
print(len(all_pairs))
possiblepair = []
for nodepair in all_pairs:
    if (nodepair[0] in mydicOfNodeCnx[nodepair[1]]) and (
            len(mydicOfNodeCnx[nodepair[0]].intersection(mydicOfNodeCnx[nodepair[1]])) == 0):
        possiblepair.append(nodepair)

print(len(possiblepair))


# possiblepair = list(combinations(possiblepair,3))


def removeCnx(dicOfNodeCnx, node1, node2):
    dicOfNodeCnx[node1].discard(node2)
    dicOfNodeCnx[node2].discard(node1)
    return dicOfNodeCnx


i = 0
for pospair in combinations(possiblepair, 3):
    newDicofCnx = copy.deepcopy(mydicOfNodeCnx)
    for pair in pospair:
        newDicofCnx = removeCnx(newDicofCnx, pair[0], pair[1])

    result = groupsCnx(newDicofCnx)
    print("i work")
    if result[0] > 1:
        print('number of groups = ', result[0], 'number of nodes in each group = ', result[1])
        break
