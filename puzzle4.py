def textTolist(file_path):
    wincardList = []
    mycardlist = []
    with open(file_path, 'r') as file:
        for line in file:
            wincard,mycard=line.split(":")[1].strip().split("|")
            wincardList.append(wincard.strip().split())
            mycardlist.append(mycard.strip().split())
    return wincardList,mycardlist

wincardList,mycardlist=textTolist('puzzle4Test.txt')
wincardList,mycardlist=textTolist('puzzle4challenge.txt')
#print(cards)

i=0
total = 0
while i< len(wincardList):
    j = 0
    score = 0
    for wCds in wincardList[i]:
        if wCds in mycardlist[i]:
            score = 2**j
            j+=1

    total = total+score
    i+=1

print('part one total',total)

def numberOfmatches(wincard,mycard):
    matches=0
    for wcds in wincard:
        if wcds in mycard:
            matches+=1
    return matches

i=0
numerofcards= [1 for _ in range(len(wincardList))]
while i < len(wincardList) and numerofcards[i]>0:
    numberOfmatch=numberOfmatches(wincardList[i],mycardlist[i])
    if (numberOfmatch >0):
        for j in range(numberOfmatch):
            numerofcards[i+j+1]=numerofcards[i+j+1] + 1*numerofcards[i]
    i+=1

print('part 2 total= ', sum(numerofcards[:]))



