'''
alllevelsallline=[]
for line in mylist:
    alllevels=[]
    alllevels.append(line)
    nextlevel=line
    while not all(element == 0 for element in nextlevel):
        nextlevel = soustractlevel(nextlevel)
        alllevels.append(nextlevel)

    alllevelsallline.append(alllevels)

print(alllevelsallline)


alllastline=[]
for line in mylist:
    lastline=[]
    lastline.append(line[-1])
    nextlevel=line
    for v in line:
        while not all(element == 0 for element in nextlevel):
            nextlevel = soustractlevel(nextlevel)
            lastline.append(nextlevel[-1])
    lastline.reverse()
    alllastline.append(lastline)
'''


def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for r, line in enumerate(file):
            mylist.append([int(num) for num in line.strip().split(" ")])
    return mylist


mylist = textTolist('puzzle9test.txt')
mylist = textTolist('puzzle9challenge.txt')


# print(mylist)

def soustractlevel(mylist):
    newlist = []
    for i in range(len(mylist) - 1):
        newlist.append(mylist[i + 1] - mylist[i])
    return newlist


def lastLine(line):
    lastline = []
    lastline.append(line[-1])
    nextlevel = line
    for v in line:
        while not all(element == 0 for element in nextlevel):
            nextlevel = soustractlevel(nextlevel)
            lastline.append(nextlevel[-1])
    lastline.reverse()
    return lastline


def reversePredict(lastLine):
    predict = []
    predict.append(lastLine[0])
    for i in range(len(lastLine) - 1):
        predict.append(lastLine[i + 1] + predict[-1])
    return predict


total = 0
for line in mylist:
    total += reversePredict(lastLine(line))[-1]

print(total)

def firsttLine(line):
    lastline = []
    lastline.append(line[0])
    nextlevel = line

    while not all(element == 0 for element in nextlevel):
        nextlevel = soustractlevel(nextlevel)
        lastline.append(nextlevel[0])
    lastline.reverse()
    return lastline


def reversePredictbackword(lastLine):
    predict = []
    predict.append(lastLine[0])
    for i in range(len(lastLine) - 1):
        predict.append(lastLine[i + 1] - predict[-1])
    return predict

total = 0
for line in mylist:
    total += reversePredictbackword(firsttLine(line))[-1]

print(total)