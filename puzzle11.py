from itertools import combinations
def textToMatrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            rows = []
            for char in line.strip():
                rows.append(char)
            matrix.append(rows)
    return matrix


pathTest = "puzzle11test.txt"
pathChallenge = "puzzle11challenge.txt"
spaceMap = textToMatrix(pathTest)
#spaceMap = textToMatrix(pathChallenge)


# print(len(spaceMap),len(spaceMap[0]))


# spaceMap = textToMatrix(pathChallenge)

def spaceExpansion(myspacemap):
    modifiedspacemap = [list(row) for row in myspacemap]
    m = 0
    for r, row in enumerate(myspacemap):
        if all(x == '.' for x in row):
            m += 1
            modifiedspacemap.insert(r + m, row)
    m = 0
    for c in range(len(myspacemap[0])):
        column = [row[c] for row in myspacemap]
        if all(x == '.' for x in column):
            m += 1
            for r in modifiedspacemap:
                r.insert(c + m, '.')

    return modifiedspacemap


spaceMap = spaceExpansion(spaceMap)
# [print(row) for row in spaceMap]
print(len(spaceMap), len(spaceMap[0]))
listofgalaxy = []
for x in range(len(spaceMap)):
    for y in range(len(spaceMap[0])):
        if spaceMap[x][y] == '#':
            listofgalaxy.append((x, y))

# print(listofgalaxy)
distance = 0

for i, gxy1 in enumerate(listofgalaxy):
    for gxy2 in listofgalaxy[i:]:
        distance += abs(gxy1[0] - gxy2[0]) + abs(gxy1[1] - gxy2[1])

print(distance)

'''
A(x,y) B(x+10**6*EmptyC+nonEmptyC,y+10**6EmptyR+nonEmptyR)
'''
pathTest = "puzzle11test.txt"
pathChallenge = "puzzle11challenge.txt"
spaceMap = textToMatrix(pathTest)
spaceMap = textToMatrix(pathChallenge)
#[print(row) for row in spaceMap]
listofgalaxy = []
for x in range(len(spaceMap)):
    for y in range(len(spaceMap[0])):
        if spaceMap[x][y] == '#':
            listofgalaxy.append((x, y))

def spaceExpansionSimulation(A,B,myspacemap):
    b=max(A[0],B[0])
    a=min(A[0],B[0])
    EmptyRow = 0
    nonEmptyRow =0
    for r in range(len(spaceMap[a+1:b])):
        if all(x == '.' for x in spaceMap[a+r+1] ):
            EmptyRow += 1
        else:
            nonEmptyRow += 1

    b = max(A[1], B[1])
    a = min(A[1], B[1])
    EmptyColumn=0
    nonEmptyColumn = 0
    for c in range(len(myspacemap[0][a+1:b])):
        k=a+c+1
        column = [row[a+c+1] for row in myspacemap]
        if all(x == '.' for x in column):
            EmptyColumn += 1
        else:
            nonEmptyColumn +=1


    return (EmptyRow ,nonEmptyRow) ,(EmptyColumn,nonEmptyColumn)

def distancebetweenA_B(A,B,myspacemap,M):
    rox,cox=spaceExpansionSimulation(A, B, myspacemap)
    ra = max(A[0], B[0])
    rb = min(A[0], B[0])
    ya = max(A[1], B[1])
    yb = min(A[1], B[1])

    distanceAB =ra-rb +rox[0]*(M-1) + ya-yb+cox[0]*(M-1)
    return distanceAB

distance=0
for A, B in combinations(listofgalaxy, 2):
    distance+= distancebetweenA_B(A, B, spaceMap, 1000000)


print(distance)



