import copy


def textToMatrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            rows = []
            for char in line.strip():
                rows.append(char)
            matrix.append(rows)
    return matrix


pathTest = "puzzle14test.txt"
pathChallenge = "puzzle14challenge.txt"
grid = textToMatrix(pathTest)
grid = textToMatrix(pathChallenge)


# [print(r) for r in grid]
def movenorth(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if grid[x][y] == 'O':
                j = x - 1
                while (0 <= j) and grid[j][y] == '.':
                    grid[j][y] = 'O'
                    grid[x][y] = '.'
                    x -= 1
                    j = x - 1
    return grid


def movesouth(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            x = len(grid) - x - 1
            if grid[x][y] == 'O':
                j = x + 1
                while (j < len(grid)) and grid[j][y] == '.':
                    grid[j][y] = 'O'
                    grid[x][y] = '.'
                    x += 1
                    j = x + 1
    return grid


def moveeast(grid):
    for row in grid:
        for x in range(len(grid[0])):
            x = len(grid[0]) - x - 1
            if row[x] == 'O':
                j = x + 1
                while j < len(grid[0]) and row[j] == '.':
                    row[j] = 'O'
                    row[x] = '.'
                    x += 1
                    j = x + 1
    return grid


def movewest(grid):
    for row in grid:
        for x in range(len(grid[0])):
            if row[x] == 'O':
                j = x - 1
                while 0 <= j < len(grid[0]) and row[j] == '.':
                    row[j] = 'O'
                    row[x] = '.'
                    x -= 1
                    j = x - 1
    return grid


# print('-----------------------------')
# [print(r) for r in grid]

total = 0
for x in range(len(grid)):
    total += grid[x].count('O') * (len(grid) - x)

print(total)

pathTest = "puzzle14test.txt"
pathChallenge = "puzzle14challenge.txt"
grid = textToMatrix(pathTest)
grid = textToMatrix(pathChallenge)


# grid=textToMatrix(pathChallenge)

# [print(r) for r in grid]
# print('-----------------------------')
def cyclemygrid(grid):
    grid = movenorth(grid)
    grid = movewest(grid)
    grid = movesouth(grid)
    grid = moveeast(grid)
    return grid


cycles = []
cycles.append(copy.deepcopy(grid))
found = False
j = 0
while not found:
    cycles.append(copy.deepcopy(cyclemygrid(grid)))
    j += 1
    if cycles[-1] in cycles[:-1]:
        found = True


a = cycles[:-1].index(cycles[-1])
b = len(cycles[:-1])
k=((1000000000-a)%(b-a)+a)
grid=cycles[k]
total = 0
for x in range(len(grid)):
    total += grid[x].count('O') * (len(grid) - x)

print(total)