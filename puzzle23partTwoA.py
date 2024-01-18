import networkx as nx


def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for line in file:
            mylist.append(line.replace('v', '.').replace('<', '.').replace('>', '.').replace('^', '.').strip())
    return mylist


#map = textTolist("puzzle23test.txt")
map = textTolist('puzzle23challenge.txt')
print(len(map), len(map[0]))
for i in range(len(map)):
    print(map[i])

G = nx.DiGraph()

def findStartandFinsh_point(matrix):
    for i in range(len(matrix[0])):
        if matrix[0][i] == '.':
            starPoint = str(0) + '*' + str(i)
            break
    for j in range(len(matrix[len(matrix) - 1])):
        if matrix[len(matrix) - 1][j] == '.':
            finish_point = str(len(matrix) - 1) + '*' + str(j)
    return starPoint, finish_point


def searchForIntesection(matrix):
    intersNodedict = {}
    for x, row in enumerate(matrix):
        for y, node in enumerate(row):
            neighborNode = []
            if node == "#":
                continue
            neighbor = 0
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (0 <= nx < len(matrix)) and (0 <= ny < len(matrix[0])) and (matrix[nx][ny] != '#'):
                    neighbor += 1
                    neighborNode.append(str(nx) + '*' + str(ny))
            if neighbor >= 3:
                intersNodedict[str(x) + '*' + str(y)]=neighborNode

    return intersNodedict

insectionNodeDict = searchForIntesection(map)
insectionNode=list(insectionNodeDict.keys())
start, destination = findStartandFinsh_point(map)
print(start, destination)
insectionNode.append(start)
insectionNode.append(destination)
print(insectionNode)
def mapping_from_A_to_node(graph,matrix,startNode,intersectionode,visitednode):
    x0 = int(startNode.split('*')[0])
    y0 = int(startNode.split('*')[1])
    curr_node = str(x0) + '*' + str(y0)
    visitednode.append(curr_node)
    x= int(startNode.split('*')[0])
    y= int(startNode.split('*')[1])
    neihborFlag = True
    steps=0
    while neihborFlag:
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            next_node=str(nx) + '*' + str(ny)
            neihborFlag=False
            if (0 <= nx < len(matrix)) and (0 <= ny < len(matrix[0])) and (matrix[nx][ny] != '#') and (next_node not in visitednode) :
                neihborFlag = True
                visitednode.append(next_node)
                next_node=str(nx) + '*' + str(ny)
                steps+=1
                if (next_node in intersectionode) and (next_node !=curr_node):
                    graph.add_edge(str(x0) + '*' + str(y0), str(nx) + '*' + str(ny),weight=steps)
                    graph.add_edge(str(nx) + '*' + str(ny), str(x0) + '*' + str(y0), weight=steps)
                    neihborFlag = False
                    break
                x=nx
                y=ny
                break
    return next_node,steps,visitednode


for node in list(insectionNodeDict.keys()):
    visitednodes=[]
    for cnx in insectionNodeDict[node]:
        next_node, steps, branchVisted = mapping_from_A_to_node(G,map,node,insectionNode,visitednodes)
        visitednodes.extend(branchVisted)


#print(mapping_from_A_to_node(G,map,'0*1',insectionNode),[])
print(G)
for edge in G.edges(data=True):
    node1, node2, attributes = edge
    weight = attributes['weight']
    print(f"Edge: ({node1}, {node2}), Weight: {weight}")


all_paths = list(nx.all_simple_paths(G, source=start,target=destination))

total_weight = []
for path in all_paths:
    total_weight.append(sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1)))

print(max(total_weight))
