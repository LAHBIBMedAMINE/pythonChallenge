def tableData(example):
    Totallist = example.strip().split(':')[1]
    sets = Totallist.strip().replace(",", "").split(';')
    listofsets = []
    for seti in sets:
        listofsets.append(seti.strip().split(" "))

    return listofsets


def checkFunCube(listofSets, ParmsBlue, ParmsRed, ParmsGreen):
    flag = True
    for s2t in listofSets:
        for i in range(len(s2t)):
            if s2t[i] == "blue":
                if int(s2t[i - 1]) > ParmsBlue:
                    flag = False
                    return flag
                    break
            elif s2t[i] == "red":
                if int(s2t[i - 1]) > ParmsRed:
                    flag = False
                    return flag
                    break
            elif s2t[i] == "green":
                if int(s2t[i - 1]) > ParmsGreen:
                    flag = False
                    return flag
                    break
    return flag


def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for line in file:
            mylist.append(line.strip())
    return mylist


mylist = textTolist("puzzle2challenge.txt")
total = 0
for i in range(len(mylist)):
    if checkFunCube(tableData(mylist[i]), 14, 12, 13):
        '''print(i+1,mylist[i])'''
        total = total + (i + 1)

print('puzzel part one total= ', total)


def minmumvalueofCubes(lsit):
    maxBlue = 0
    maxRed = 0
    maxGreen = 0
    for s2t in lsit:
        for i in range(len(s2t)):
            if s2t[i] == "blue":
                if int(s2t[i - 1]) > maxBlue:
                    maxBlue = int(s2t[i - 1])
            elif s2t[i] == "red":
                if int(s2t[i - 1]) > maxRed:
                    maxRed = int(s2t[i - 1])
            elif s2t[i] == "green":
                if int(s2t[i - 1]) > maxGreen:
                    maxGreen = int(s2t[i - 1])
    print('maxRed= ', maxRed, ' maxGreen= ', maxGreen, ' maxBlue= ', maxBlue, '// powerOfCubes = ',
          maxRed * maxGreen * maxBlue)
    return (maxRed * maxGreen * maxBlue)


total = 0
for i in range(len(mylist)):
    total = total + minmumvalueofCubes(tableData(mylist[i]))

print('the Total Power= ', total)
