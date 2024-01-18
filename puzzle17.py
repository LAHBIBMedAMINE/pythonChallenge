from heapq import heappush, heappop


def textToMatrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            rows = []
            for char in line.strip():
                rows.append(int(char))
            matrix.append(rows)
    return matrix


pathTest = "puzzle17test.txt"
pathChallenge = "puzzle17challenge.txt"
grid = textToMatrix(pathTest)
grid = textToMatrix(pathChallenge)
# [print(row) for row in grid]
print(len(grid), len(grid[0]))

visited = set()

# heatloss,x,y,dx,dy,n
step = [(0, 0, 0, 0, 0, 0)]

while step:
    heatloss, x, y, dx, dy, n = heappop(step)

    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        print(heatloss)
        break

    if (x, y, dx, dy, n) in visited:
        continue

    visited.add((x, y, dx, dy, n))

    if n < 3 and (dx, dy) != (0, 0):
        ndx = x + dx
        ndy = y + dy
        if 0 <= ndx < len(grid) and 0 <= ndy < len(grid[0]):
            heappush(step, (heatloss + grid[ndx][ndy], ndx, ndy, dx, dy, n + 1))

    for (sx, sy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (sx, sy) != (dx, dy) and (sx, sy) != (-dx, -dy):
            ndx = x + sx
            ndy = y + sy
            if 0 <= ndx < len(grid) and 0 <= ndy < len(grid[0]):
                heappush(step, (heatloss + grid[ndx][ndy], ndx, ndy, sx, sy, 1))

pathTest = "puzzle17test.txt"
pathChallenge = "puzzle17challenge.txt"
grid = textToMatrix(pathTest)
grid = textToMatrix(pathChallenge)
visited = set()

# heatloss,x,y,dx,dy,n
step = [(0, 0, 0, 0, 0, 0)]

while step:
    heatloss, x, y, dx, dy, n = heappop(step)

    if x == len(grid) - 1 and y == len(grid[0]) - 1 and n >= 4:
        print(heatloss)
        break

    if (x, y, dx, dy, n) in visited:
        continue

    visited.add((x, y, dx, dy, n))

    if n < 10 and (dx, dy) != (0, 0):
        ndx = x + dx
        ndy = y + dy
        if 0 <= ndx < len(grid) and 0 <= ndy < len(grid[0]):
            heappush(step, (heatloss + grid[ndx][ndy], ndx, ndy, dx, dy, n + 1))

    if n >= 4 or (dx, dy) == (0, 0):
        for (sx, sy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (sx, sy) != (dx, dy) and (sx, sy) != (-dx, -dy):
                ndx = x + sx
                ndy = y + sy
                if 0 <= ndx < len(grid) and 0 <= ndy < len(grid[0]):
                    heappush(step, (heatloss + grid[ndx][ndy], ndx, ndy, sx, sy, 1))
