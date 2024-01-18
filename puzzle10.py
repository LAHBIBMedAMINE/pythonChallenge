def textToMatrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            matrix.append(line.strip())
    return matrix


pathTest = "puzzle10test2.txt"
pathChallenge = "puzzle10challenge.txt"
maps = textToMatrix(pathTest)
maps = textToMatrix(pathChallenge)




directionRluses = {}
directionRluses['S'] = [((-1, 0), ('F', '|', '7')), ((1, 0), ('L', '|', 'J')), ((0, 1), ('7', '-', 'J')),
                        ((0, -1), ('L', '-', 'F'))]
directionRluses['-'] = [((0, -1), ('-', 'L', 'F')), ((0, 1), ('-', '7', 'J'))]
directionRluses['|'] = [((-1, 0), ('F', '|', '7')), ((1, 0), ('L', '|', 'J'))]
directionRluses['F'] = [((0, 1), ('-', 'J', '7')), ((1, 0), ('L', '|', 'J'))]
directionRluses['L'] = [((0, 1), ('-', 'J', '7')), ((-1, 0), ('F', '|', '7'))]
directionRluses['7'] = [((0, -1), ('-', 'L', 'F')), ((1, 0), ('|', 'L', 'J'))]
directionRluses['J'] = [((0, -1), ('-', 'L', 'F')), ((-1, 0), ('|', '7', 'F'))]


# print(directionRluses)
def searchForS(mymaps, symbol):
    for r, row in enumerate(mymaps):
        if symbol in row:
            c = row.index(symbol)
            break
    return (r, c)


def checknextpipe(mymap, curr_pipe, directionDict, myvisitedpipe):
    x, y = curr_pipe
    for d in directionDict[mymap[x][y]]:
        d, possibe_pipe = d
        if 0 <= x + d[0] < len(mymap) and 0 <= y + d[1] < len(mymap[0]) and (x + d[0], y + d[1]) not in myvisitedpipe:
            if mymap[x + d[0]][y + d[1]] in possibe_pipe:
                x = x + d[0]
                y = y + d[1]
                startpoint = False
                return (x, y)
                break

    return (x, y)


stepvisited = []
startPoint = searchForS(maps, 'S')
stepvisited.append(startPoint)  # start
stepvisited.append(checknextpipe(maps, stepvisited[-1], directionRluses, stepvisited))  # first step
while stepvisited[-1] != stepvisited[0]:
    curr_pos = stepvisited[-1]
    stepvisited.append(checknextpipe(maps, curr_pos, directionRluses, stepvisited))
    if stepvisited[-1] == stepvisited[-2]:
        stepvisited = stepvisited[:-1]
        break

# print(stepvisited)
print((len(stepvisited) / 2))

for x,r in enumerate(maps):
    for y,c in enumerate(r):
        if (x,y) not in stepvisited:
            maps[x]=maps[x][:y]+'.'+maps[x][y+1:]


maps[startPoint[0]]=maps[startPoint[0]].replace('S','|')

outsider = []
insider = []
for x, r in enumerate(maps):
    for y, c in enumerate(r):
        if c == '.':
            edg = 0
            r1=r[y:].replace('-','').replace('F7','').replace('LJ','')
            for el in r1:
                if el in ['L', 'J', '7', 'F']:
                    edg += 0.5
                elif el == '|':
                    edg += 1
            if edg % 2 == 0 or edg==0:
                outsider.append((x, y))
            elif edg % 2 == 1:
                insider.append((x, y))

print('outsider', len(outsider))
print('insider', len(insider))

