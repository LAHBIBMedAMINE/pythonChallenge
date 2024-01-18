''' Resolving Y
xA = b + a*t /// xB = b' + a'*t
yA = c + d*t ///  yB = c' + d'*t
t = (yA-c)/d /// t = (yB-c')/d'
xA= b -(a*c/d)+(a/d)y /// xB =b' -(a'*c'/d')+(a'/d')yB
xA=xB and yA = yB  ===>
K = b -(a*c/d) /// k'= b' -(a'*c'/d')
m= a/d/// m' =a'/d'
xA=xB and yA = yB =y  ===> k + m*y = k' + m'*y ==> y = k-k'/m'-m
same for X
x = (k-k')/(m'-m) with k=c-(d*b/a) and m=d/a'''
'''
b1= hailstoneA[0]
a1= hailstoneA[4]
c1= hailstoneA[1]
d1= hailstoneA[5]
////////////
b2= hailstoneB[0]
a2= hailstoneB[4]
c2= hailstoneB[1]
d2= hailstoneB[5]
'''
'''
y = ((b1 - ((a1*c1)/d1))-(b2 - ((a2*c2)/d2))) / ((a2/d2)-(a1/d1))
x = ((c1 - ((d1*b1)/a1)) - (c2 - ((d2*b2)/a2))) / ((d2/a2) - (d1/a1))
print(x,y)
'''
def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for line in file:
            mylist.append(line.strip())
    return mylist
testFilePath="puzzel24Test.txt"
challengeFilePath="puzzel24challenge.txt"

#rawFile =textTolist(testFilePath)
rawFile =textTolist(challengeFilePath)

def tableData(rawFile):
    listofvectors=[]
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

def checkIntersection(hailstoneA,hailstoneB,lowerlimitx,upperlimitx,lowerlimity,upperlimity):
    if (hailstoneA[4]/hailstoneA[5])==(hailstoneB[4]/hailstoneB[5]):
        #vector = [(abs(b1-b2)),(abs(c1-c2))]
        print('no intersection')
        return False
    else:
        y = ((hailstoneA[0] - ((hailstoneA[4] * hailstoneA[1]) / hailstoneA[5])) - (hailstoneB[0] - ((hailstoneB[4] * hailstoneB[1]) / hailstoneB[5]))) / ((hailstoneB[4] / hailstoneB[5]) - (hailstoneA[4] / hailstoneA[5]))
        x = ((hailstoneA[1]- ((hailstoneA[5] * hailstoneA[0]) / hailstoneA[4])) - (hailstoneB[1] - ((hailstoneB[5] * hailstoneB[0]) / hailstoneB[4]))) / ((hailstoneB[5] / hailstoneB[4]) - (hailstoneA[5] / hailstoneA[4]))
        if (lowerlimitx<x<upperlimitx) and (lowerlimity<y<upperlimity):
            if ((((x-hailstoneA[0])/hailstoneA[4])<0) or (((x-hailstoneB[0])/hailstoneB[4])<0)):
                print("cross path inside the area in the past",f"X= {x:.3f}",f"Y= {y:.3f}")
                return False

            elif ((((x-hailstoneA[0])/hailstoneA[4])>0) and (((x-hailstoneB[0])/hailstoneB[4])>0)):
                print("cross path inside the area in the future", f"X= {x:.3f}", f"Y= {y:.3f}")
                return True

        else:
            if ((((x - hailstoneA[0]) / hailstoneA[4]) < 0) or (((x - hailstoneB[0]) / hailstoneB[4]) < 0)):
                print("cross path outside the area in the past", f"X= {x:.3f}", f"Y= {y:.3f}")
                return False
            elif ((((x - hailstoneA[0]) / hailstoneA[4]) > 0) and (((x - hailstoneB[0]) / hailstoneB[4]) > 0)):
                print("cross path outside the area in the future", f"X= {x:.3f}", f"Y= {y:.3f}")
                return False
table=tableData(rawFile)
print()

count=0
for i in range(len(table)):
    j=i+1
    while j < len(table):
        if (checkIntersection(table[i],table[j],200000000000000,400000000000000,200000000000000,400000000000000)):
            count+=1
        j+=1
print('total future crossing in the area = ', count)