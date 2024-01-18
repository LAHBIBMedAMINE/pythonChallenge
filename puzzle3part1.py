import numpy as np


def textToMatrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            rows = []
            for char in line.strip():
                rows.append(char)
            matrix.append(rows)
    return matrix


pathTest = "testpuzzel3.txt"
pathChallenge = "inputpuzzel3.txt"
enginDoc = np.array(textToMatrix(pathTest))
enginDoc = np.array(textToMatrix(pathChallenge))
print("originalDoc")
print(enginDoc)

''' I will make all different symbol '*' '/' to 'S' '''
for i in range(enginDoc.shape[0]):
    for j in range(enginDoc.shape[1]):
        value = str(enginDoc[i, j])
        if (value != '.') and not (value.isdigit()):
            enginDoc[i, j] = 'S'

print("modified symbol Doc")
print(enginDoc)


def checkSurround(matrix, i, j, symbol):
    # check up
    if (i - 1 >= 0) and (str(matrix[i - 1, j]) == symbol):
        return True
    # check down
    elif (i + 1 < matrix.shape[0]) and (str(matrix[i + 1, j]) == symbol):
        return True
    # check right
    elif (j - 1 >= 0) and (str(matrix[i, j - 1]) == symbol):
        return True
    # check down
    elif (j + 1 < matrix.shape[1]) and (str(matrix[i, j + 1]) == symbol):
        return True
    # check up right corner
    elif ((i - 1 >= 0) and (j - 1 > 0)) and (str(matrix[i - 1, j - 1]) == symbol):
        return True
    # check down right corner
    elif ((i+1<matrix.shape[0]) and (j-1>=0)) and (str(matrix[i + 1, j - 1]) == symbol):
        return True
    # check up left corner
    elif ((i-1>=0) and (j+1<matrix.shape[1])) and (str(matrix[i - 1, j + 1]) == symbol):
        return True
    # check down left corner
    elif ((i+1<matrix.shape[0]) and (j+1<matrix.shape[1])) and (str(matrix[i + 1, j + 1]) == symbol):
        return True
    else:
        return False


def extractTheDigits(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if str(matrix[i, j]).isdigit() and (checkSurround(matrix, i, j, 'S')):
                matrix[i, j] = True
            k=j
            if (matrix[i,j]=='T'):
                while ((k-1>=0) and ((matrix[i,k-1]=='T') or str(matrix[i,k-1]).isdigit())):
                    matrix[i,k-1]=True
                    k-=1

                while (k+1 < matrix.shape[1]) and ((matrix[i,k+1] == 'T') or str(matrix[i,k+1]).isdigit()):
                    matrix[i,k+1]=True
                    k+=1

    return matrix

def extractsum(map,originalMatrix):
    listofnumber=[]
    for i in range(map.shape[0]):
        j=-1

        while (j+1 < map.shape[1]):
            if (map[i,j+1]=='T'):
                s = str(originalMatrix[i,j+1])
                k=j+1
                while (k+1<map.shape[1]) and (map[i,k+1]=='T'):
                    s=s+str(originalMatrix[i,k+1])
                    k+=1
                    j=k
                listofnumber.append(s)

            s=[]
            j+=1

    return [listofnumber,sum(int(num) for num in listofnumber)]








mymap = enginDoc.copy()
mymap = extractTheDigits(mymap)
print("(-----------*-----------------)")
result = extractsum(mymap,enginDoc)
print("(-----------list of gear digit-----------------)")
print(result[0])
print("(-----------Total-----------------)")
print(result[1])