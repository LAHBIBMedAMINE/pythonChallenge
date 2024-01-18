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
# enginDoc = np.array(textToMatrix(pathTest))
enginDoc = np.array(textToMatrix(pathChallenge))
print('(-----------------"originalDoc"------------------------------------)')
print(enginDoc)




def checkSurroundSymbol(matrix):
    symbolCord = []
    elments=[]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            count = 0

            if matrix[i, j] == '*':
                elm1 = None
                elm2 = None
                elm3 = None
                elm4 = None
                elm5 = None
                elm6 = None
                elm7 = None
                elm8 = None
                elms = []

                # check up
                if (i - 1 >= 0) and (str(matrix[i - 1, j]).isdigit()):
                    elm1 =str(matrix[i - 1, j])
                    matrix[i - 1, j] = True
                    count += 1
                    m = i - 1
                    k = j
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm1 = str(matrix[m, k-1]) + elm1
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm1 = elm1 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1

                    elms.append(elm1)


                # check down
                if (i + 1 < matrix.shape[0]) and (str(matrix[i + 1, j]).isdigit()):
                    elm2 = str(matrix[i + 1, j])
                    matrix[i + 1, j] = True
                    count += 1
                    m = i + 1
                    k = j
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm2 = str(matrix[m, k - 1]) + elm2
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm2 = elm2 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1

                    elms.append(elm2)

                # check right
                if (j - 1 >= 0) and (str(matrix[i, j - 1]).isdigit()):
                    elm3 = str(matrix[i, j - 1])
                    matrix[i, j - 1] = True
                    count += 1
                    m = i
                    k = j - 1
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm3 = str(matrix[m, k - 1]) + elm3
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j - 1
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm3 = elm3 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1

                    elms.append(elm3)

                # check down
                if (j + 1 < matrix.shape[1]) and (str(matrix[i, j + 1]).isdigit()):
                    elm4 = str(matrix[i, j + 1])
                    matrix[i, j + 1] = True
                    count += 1
                    m = i
                    k = j + 1
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm4 = str(matrix[m, k - 1]) + elm4
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j + 1
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm4 = elm4 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1

                    elms.append(elm4)

                # check up right corner
                if ((i - 1 >= 0) and (j - 1 >= 0)) and (str(matrix[i - 1, j - 1]).isdigit()):
                    elm5 = str(matrix[i - 1, j - 1] )
                    matrix[i - 1, j - 1] = True
                    count += 1
                    m = i - 1
                    k = j - 1
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm5 = str(matrix[m, k - 1]) + elm5
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j - 1
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm5 = elm5 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1

                    elms.append(elm5)
                # check down right corner
                if ((i + 1 < matrix.shape[0]) and (j - 1 >= 0)) and (str(matrix[i + 1, j - 1]).isdigit()):
                    elm6 = str(matrix[i + 1, j - 1])
                    matrix[i + 1, j - 1] = True
                    count += 1
                    m = i + 1
                    k = j - 1
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm6 = str(matrix[m, k - 1]) + elm6
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j - 1
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm6 = elm6 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1

                    elms.append(elm6)

                # check up left corner
                if ((i - 1 >= 0) and (j + 1 < matrix.shape[1])) and (str(matrix[i - 1, j + 1]).isdigit()):
                    elm7 = str(matrix[i - 1, j + 1])
                    matrix[i - 1, j + 1] = True
                    count += 1
                    m = i - 1
                    k = j + 1
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm7 = str(matrix[m, k - 1]) + elm7
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j + 1
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm7 = elm7 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1

                    elms.append(elm7)

                # check down left corner
                if ((i + 1 < matrix.shape[0]) and (j + 1 < matrix.shape[1])) and (str(matrix[i + 1, j + 1]).isdigit()):
                    elm8 = str(matrix[i + 1, j + 1])
                    matrix[i + 1, j + 1] = True
                    count += 1
                    m = i + 1
                    k = j + 1
                    while ((k - 1 >= 0) and str(matrix[m, k - 1]).isdigit()):
                        elm8 = str(matrix[m, k - 1]) + elm8
                        matrix[m, k - 1] = True
                        k -= 1
                    k = j + 1
                    while (k + 1 < matrix.shape[1]) and (str(matrix[m, k + 1]).isdigit()):
                        elm8 = elm8 + str(matrix[m, k + 1])
                        matrix[m, k + 1] = True
                        k += 1
                    elms.append(elm8)

                if (count == 2):
                    symbolCord.append([i, j])
                    for el in elms:
                        if (el is not None):
                            elments.append(el)

    i = 0
    mysum = 0
    while i < len(elments):
        mysum = mysum + int(elments[i]) * int(elments[i + 1])
        i += 2
    return [symbolCord,elments,mysum]


targetlist = enginDoc.copy()
print('(-----------------result-----------------------------------------------------------)')
targetlist = checkSurroundSymbol(targetlist)
print('(-----------------list of coordination of gear2------------------------------------)')
print(targetlist[0])
print('(-----------------list of elements of gear2----------------------------------------)')
print(targetlist[1])
print('(-----------------Total------------------------------------------------------------)')
print(targetlist[2])


for item in targetlist[0]:
    print('(-----------------', item, '------------------------------------)')
    print(enginDoc[item[0] - 1:item[0] + 3, item[1] - 5:item[1] + 5])
