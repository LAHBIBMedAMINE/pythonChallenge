import math

print('(---------------------------------PartOne-----------------------------------------)')
print("step 1 convert file to steps='LLR' and dictionary key='AAA':value='BBB','CCC'")
def textTodict(file_path):
    stepDict = {}
    with open(file_path, 'r') as file:
        puzzle_input = file.read()

    segments = puzzle_input.split('\n')
    segments = [x for x in segments if x != ""]
    steps=segments[0]

    for step in segments[1:]:
        stepDict[step.split(" = ")[0].strip()]=tuple(step.split(" = ")[1].strip('()').split(', '))


    return steps,stepDict

steps,stepDict=textTodict('puzzle8test.txt')
#steps,stepDict=textTodict('puzzle8challenge.txt')
#print(steps)
#print(stepDict)

#print(len(steps))
print("step 2 Navigating and counting the steps")
steplen=len(steps)
counter=len(steps)
j=0
found=False
curr_node = 'AAA'
while not found :
    counter %= len(steps)
    if steps[counter] == 'L':
        curr_node=stepDict[curr_node][0]
        if (curr_node=='ZZZ'):
            found=True
    else:
        curr_node = stepDict[curr_node][1]
        if (curr_node=='ZZZ'):
            found=True
    counter+=1
    j+=1

print('total of steps= ',j)
print('(---------------------------------PartOne-----------------------------------------)')
print("step 1 convert file to steps='LLR' and dictionary key='AAA':value='BBB','CCC'")
steps,stepDict=textTodict('puzzle8txtpart2.txt')
steps,stepDict=textTodict('puzzle8challenge.txt')
print("step 2 search for starting Nodes'")
startingNode = [key for key,value in stepDict.items() if key[2]=='A']
print(startingNode)

print("step 3 search when every node reach XXZ'")
steplen=len(steps)
counter=len(steps)
startingNode
numberOFsteopToreach_Z=[]
for node in startingNode:
    found=False
    j = 0
    while not found :
        counter %= len(steps)
        if steps[counter] == 'L':
            node = stepDict[node][0]
            if (node[2] == 'Z'):
                found = True
        else:
            node = stepDict[node][1]
            if (node[2] == 'Z'):
                found = True
        counter += 1
        j += 1
    numberOFsteopToreach_Z.append(j)

#brute force will take years
print(numberOFsteopToreach_Z)
print("step 4 play the math for Least Common Multiple **brute force takes years** :p)")
print('total of steps= ', math.lcm(*numberOFsteopToreach_Z))