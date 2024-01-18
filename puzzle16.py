from collections import deque

def textToMatrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            rows = []
            for char in line.strip():
                rows.append(char)
            matrix.append(rows)
    return matrix


pathTest = "puzzle16test.txt"
pathChallenge = "puzzle16challenge.txt"
grid = textToMatrix(pathTest)
grid = textToMatrix(pathChallenge)
#[print(row) for row in grid]
#print(len(grid),len(grid[0]))

def calculateMEnergie(A,grid):
    # x,y,dx,dy
    #A=[(0,-1,0,1)]
    visited =set()
    steps=deque(A)

    while steps:
        x,y,dx,dy=steps.popleft()
        x+=dx
        y+=dy

        if x<0 or x >= len(grid) or y<0 or y >= len(grid[0]):
            continue

        if grid[x][y] =='.':
            if (x,y,dx,dy) not in visited:
                visited.add((x,y,dx,dy))
                steps.append((x,y,dx,dy))
        elif grid[x][y] =='|':
            if (x, y, dx, dy) not in visited:
                visited.add((x, y, dx, dy))
                if dx !=0:
                    steps.append((x, y, dx, dy))
                elif dy !=0:
                    steps.append((x,y,-1,0))
                    steps.append((x,y,1,0))
        elif grid[x][y]=='-':
            if (x, y, dx, dy) not in visited:
                visited.add((x, y, dx, dy))
                if dy !=0:
                    steps.append((x, y, dx, dy))
                elif dx !=0:
                    steps.append((x,y,0,-1))
                    steps.append((x,y,0,1))
        elif grid[x][y] == "/":
            dx, dy = -dy, -dx
            if (x,y , dx, dy) not in visited:
                visited.add((x, y, dx, dy))
                steps.append((x, y, dx, dy))
        elif grid[x][y] == "\\":
            dx, dy = dy, dx
            if (x, y, dx, dy) not in visited:
                visited.add((x, y, dx, dy))
                steps.append((x, y, dx, dy))

    coords = {(x, y) for (x, y, _, _) in visited}
    return len(coords)

#print(calculateMEnergie([(0,-1,0,1)],grid))

maxleft =max([calculateMEnergie([(x,-1,0,1)],grid)  for x in range(len(grid))])
maxright =max([calculateMEnergie([(x,len(grid[0]),0,-1)],grid)  for x in range(len(grid))])
maxup =max([calculateMEnergie([(-1,y,1,0)],grid)  for y in range(len(grid[0]))])
maxdown =max([calculateMEnergie([(len(grid),y,-1,0)],grid)  for y in range(len(grid[0]))])
print(maxleft,maxright,maxup,maxdown,max([maxleft,maxright,maxup,maxdown]))