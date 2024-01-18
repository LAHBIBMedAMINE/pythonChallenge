import re
def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for r, line in enumerate(file):
            d, num, color = line.strip().split(' ')
            mylist.append([d, int(num), color])
    return mylist


test_path = "puzzle18test.txt"
challenge_path = 'puzzle18challenge.txt'
maps = textTolist(test_path)
maps=textTolist(challenge_path)
# [print(line) for line in maps]

cord = (0, 0)
steps = []
for line in maps:
    if line[0] == 'R':
        for i in range(line[1] + 1):
            if (cord[0], cord[1] + i) not in steps:
                steps.append((cord[0], cord[1] + i))
        cord = steps[-1]
    elif line[0] == 'D':
        for i in range(line[1] + 1):
            if (cord[0] + i, cord[1]) not in steps:
                steps.append((cord[0] + i, cord[1]))
        cord = steps[-1]
    elif line[0] == 'U':
        for i in range(line[1] + 1):
            if (cord[0] - i, cord[1]) not in steps:
                steps.append((cord[0] - i, cord[1]))
        cord = steps[-1]
    elif line[0] == 'L':
        for i in range(line[1] + 1):
            if (cord[0], cord[1] - i)not in steps:
                steps.append((cord[0], cord[1] - i))
        cord = steps[-1]

k=min([item[0] for item in steps])
m=min([item[1] for item in steps])
for i in range(len(steps)):
    steps[i]=(steps[i][0]-k,steps[i][1]-m)
r = max([item[0] for item in steps]) + 1
c = max([item[1] for item in steps]) + 1

grid = [['#' if (x,y) in steps else '.' for y in range(c)] for x in range(r)]

#[print(row) for row in grid]
n=len(steps)
#https://en.wikipedia.org/wiki/Shoelace_formula
area = 0.5 * abs(sum(steps[i][0] * steps[(i + 1) % n][1] - steps[(i + 1) % n][0] * steps[i][1] for i in range(n)))
#https://en.wikipedia.org/wiki/Pick%27s_theorem ====>number of interior point
i = area - n // 2 + 1

print(i+n)


cord = (0, 0)
steps = []
steps.append(cord)
verticelen=0
for line in maps:
    dir=line[2][-2]
    long=int(line[2][2:7], 16)
    verticelen+=long
    if dir == '0':
        steps.append((cord[0], cord[1] + long))
        cord = steps[-1]
    elif dir == '1':
        steps.append((cord[0] + long, cord[1]))
        cord = steps[-1]
    elif dir == '3':
        steps.append((cord[0] - long, cord[1]))
        cord = steps[-1]
    elif dir == '2':
        steps.append((cord[0], cord[1] - long))
        cord = steps[-1]

n=len(steps)
#https://en.wikipedia.org/wiki/Shoelace_formula
area = 0.5 * abs(sum(steps[i][0] * steps[(i + 1) % n][1] - steps[(i + 1) % n][0] * steps[i][1] for i in range(n)))
#https://en.wikipedia.org/wiki/Pick%27s_theorem ====>number of interior point
i = area - verticelen // 2 + 1

print(i+verticelen)