from collections import deque
def textToMatrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            matrix.append([char for char in line.strip()])
    return matrix

grid=textToMatrix('puzzle21test.txt')
grid=textToMatrix('puzzle21challenge.txt')
#[print(r) for r in grid]


for r,row in enumerate(grid):
    if 'S' in row:
        sx,sy=(r,row.index('S'))

#print(startposition)

gridReach=set()
visited=set()
visited.add((sx,sy))
laststeps=deque([])
laststeps.append((sx,sy,64))

while laststeps:
    (x,y,step_count)=laststeps.popleft()
    if step_count %2 ==0:
        gridReach.add((x,y))
    if step_count==0:
        continue
    for nr, nc in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in visited:
            continue
        visited.add((nr,nc))
        laststeps.append((nr,nc,step_count-1))


print(len(gridReach))