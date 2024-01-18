'''
x + y = t1
x*y = d1

x + y = 7     y=7-x ==>  x(7-x) >9 ==>  -x**2 + 7x >9
x*y > 9

x + y = 15
x*y > 40

x + y = 30
x*y >200
'''
def textTolist(file_path):
    mylist = []
    with open(file_path, 'r') as file:
        for line in file:
            mylist.append(list(filter(None,line.strip().split(":")[1].strip().split(' '))))
    return mylist

#file_path='puzzle6test.txt'
file_path='puzzle6challenge.txt'
mylist=textTolist(file_path)
print(mylist)

prod=1
count=1
for t, d in zip(mylist[0], mylist[1]):
    count = 0
    for x in range(int(t)+1):
        y=int(t)-x
        if x*y > int(d):
            count+=1
    prod = prod * count
print('prod of ways = ',prod)

T,D='',''
for t,d in zip(mylist[0], mylist[1]):
    T=T+t
    D=D+d

print('time = ',T,'distance to beat=',D)

count=0
for x in range(14,int(T),1):
    y=int(T)-x
    if x*y>int(D):
        count+=1

print(count, ' possible way')