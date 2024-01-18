import networkx as nx


def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for line in file:
            mylist.append(line.strip())
    return mylist


map = textTolist("puzzle23test.txt")
map = textTolist('puzzle23challenge.txt')
print(len(map),len(map[0]))
for i in range(len(map)):
    print(map[i])

G = nx.DiGraph()


def mapping(matrix, graph):
    rows = len(matrix)
    cols = len(matrix[0])

    for x in range(rows):
        for y in range(cols):
            # check down
            if matrix[x][y] == '.':
                if x + 1 < rows and matrix[x + 1][y] == '.':
                    graph.add_edge(str(x) + '*' + str(y), str(x + 1) + '*' + str(y))
                    graph.add_edge(str(x + 1) + '*' + str(y), str(x) + '*' + str(y))
                elif (x + 1 < rows) and (matrix[x + 1][y] in ['v', '>', '<']):
                    graph.add_edge(str(x) + '*' + str(y), str(x + 1) + '*' + str(y))
                elif (x + 1 < rows) and (matrix[x + 1][y] in ['^']):
                    graph.add_edge(str(x + 1) + '*' + str(y), str(x) + '*' + str(y))

                # check right
                if y + 1 < cols and matrix[x][y + 1] == '.':
                    graph.add_edge(str(x) + '*' + str(y), str(x) + '*' + str(y + 1))
                    graph.add_edge(str(x) + '*' + str(y + 1), str(x) + '*' + str(y))
                elif y + 1 < cols and matrix[x][y + 1] in ['v', '>','^']:
                    graph.add_edge(str(x) + '*' + str(y), str(x) + '*' + str(y + 1))
                elif y + 1 < cols and matrix[x][y + 1] in ['<']:
                    graph.add_edge(str(x) + '*' + str(y + 1), str(x) + '*' + str(y))

                # check up
                if x - 1 >= 0 and matrix[x - 1][y] == '.':
                    graph.add_edge(str(x - 1) + '*' + str(y), str(x) + '*' + str(y))
                    graph.add_edge(str(x) + '*' + str(y), str(x - 1) + '*' + str(y))
                elif x - 1 >= 0 and matrix[x - 1][y] in ['>', '<','^']:
                    graph.add_edge(str(x) + '*' + str(y), str(x - 1) + '*' + str(y))
                elif x - 1 >= 0 and matrix[x - 1][y] in ['v']:
                    graph.add_edge(str(x - 1) + '*' + str(y), str(x) + '*' + str(y))

                # Print left
                if y - 1 >= 0 and matrix[x][y - 1] == '.':
                    graph.add_edge(str(x) + '*' + str(y - 1), str(x) + '*' + str(y))
                    graph.add_edge(str(x) + '*' + str(y), str(x) + '*' + str(y - 1))
                elif y - 1 >= 0 and matrix[x][y - 1] in ['v', '<','^']:
                    graph.add_edge(str(x) + '*' + str(y), str(x) + '*' + str(y - 1))
                elif y - 1 >= 0 and matrix[x][y - 1] in ['>']:
                    graph.add_edge(str(x) + '*' + str(y - 1), str(x) + '*' + str(y))

    return graph

def findStartandFinsh_point(matrix):
    for i in range(len(matrix[0])):
        if matrix[0][i]=='.':
            starPoint=str(0)+'*'+str(i)
            break
    for j in range(len(matrix[len(matrix)-1])):
        if matrix[len(matrix)-1][j]=='.':
            finish_point= str(len(matrix)-1)+'*'+str(j)
    return starPoint,finish_point

G= mapping(map,G)
print(G)
#start = (str(0)+'*'+str(1))
#destination = (str(22)+'*'+str(21))
start,destination = findStartandFinsh_point(map)
all_paths = list(nx.all_simple_paths(G, source=start, target=destination))

all_paths = sorted(all_paths, key=lambda x: len(x))
i=1
for path in all_paths:
    print('path '+str(i)+' :','number of steps ',len(path)-1," ==>",path)
    i+=1

print('the shortest path is path 1 :','number of steps ',len(all_paths[0])-1)
print('the longest path is path ',str(len(all_paths)),' :','number of steps ',len(all_paths[len(all_paths)-1])-1)