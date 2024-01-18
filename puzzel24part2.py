import sympy as sp


def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for line in file:
            mylist.append(line.strip())
    return mylist


testFilePath = "puzzel24Test.txt"
challengeFilePath = "puzzel24challenge.txt"

# rawFile =textTolist(testFilePath)
rawFile = textTolist(challengeFilePath)


def tableData(rawFile):
    listofvectors = []
    for line in rawFile:
        lineSplited = line.strip().split('@')
        XYZ = lineSplited[0].strip().split(',')
        VxVyVz = lineSplited[1].strip().split(',')
        vector = []
        for xyz in XYZ:
            vector.append(int(xyz.strip()))
        vector.append('@')
        for vxvyvz in VxVyVz:
            vector.append(int(vxvyvz.strip()))
        listofvectors.append(vector)

    return listofvectors


listofvector = tableData(rawFile)
print(listofvector)

''' the solution consist of resolving the 3 equations of each hailstone (x,y,y)
(x0r,y0r, z0r) rock starting position *unknown*/ (dxr, dyr, dzr ) rock motion vector *unknown*
(x0,y0, z0) hailstone starting position *known* / (dx, dy, dz ) hailstone motion vector *known*
x0r + dxr*t = x0 + dx*t
y0r + dyr*t = y0 + dy*t
z0r + dzr*t = z0 + dz*t  
the sumpy allows resolving this equation'''
numberofstones = 3  # chose number of equation
''' i tried a different number of equation i found that less than 3*3 equation the system can't be solved
  for more 5*3 equation it took much time to solve it'''

unknowns = sp.symbols(
    'x y z dx dy dz t1:{}'.format(numberofstones + 1))  # t1:{}'.format(numberofstones + 1) to genrate t1 t2 t3 tx
x, y, z, dx, dy, dz, *time = unknowns  # '*time' allows to zip the remaining t1 in a list name time

equations = []  # buiding the equation system
for t, hailstone in zip(time, listofvector[0:numberofstones]):
    equations.append(sp.Eq(x + t * dx, hailstone[0] + t * hailstone[4]))
    equations.append(sp.Eq(y + t * dy, hailstone[1] + t * hailstone[5]))
    equations.append(sp.Eq(z + t * dz, hailstone[2] + t * hailstone[6]))

solution = sp.solve(equations, unknowns).pop()
print(solution)
print(sum(solution[0:3]))
