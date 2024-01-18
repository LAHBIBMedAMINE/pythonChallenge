def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for r, line in enumerate(file):
            mylist.extend(line.strip().split(','))
    return mylist
test_path="puzzle15test.txt"
challenge_path='puzzle15challenge.txt'
A=textTolist(test_path)
A=textTolist(challenge_path)

def hashalgo(A):
    t=0
    for x in A:
        t=t+ord(x)
        t=t*17
        t=t%256
    return t
total=0
for code in A:
    total+=hashalgo(code)

print(total)

boxes=[[] for _ in range(256)]
for x in A:
    if '=' in x:
        label,focal=x.split('=')
        if boxes[hashalgo(label)] and label in [lb[0] for lb in boxes[hashalgo(label)]]:
            index=[lb[0] for lb in boxes[hashalgo(label)]].index(label)
            boxes[hashalgo(label)][index]=(label,int(focal))
        else:
            boxes[hashalgo(label)].append((label,int(focal)))
    elif '-' in x:
        label=x[:-1]
        if boxes[hashalgo(label)] and label in [lb[0] for lb in boxes[hashalgo(label)]]:
            index = [lb[0] for lb in boxes[hashalgo(label)]].index(label)
            boxes[hashalgo(label)].remove(boxes[hashalgo(label)][index])


total=0
for m,box in enumerate(boxes,start=1):
    if box:
        for n,item in enumerate(box,start=1):
            total+=m*n*item[1]

#[print('box ',n,' ',box) for n,box in enumerate(boxes)]
print(total)


