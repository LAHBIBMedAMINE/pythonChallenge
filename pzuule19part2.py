import re


def textTolist(file_path):
    with open(file_path, 'r') as file:

        grid = file.read().split('\n\n')

    equation = []
    inputs = []
    for line in grid[0].split('\n'):
        equation.append(line.strip())
    for line in grid[1].split('\n'):
        inputs.append(line.strip())
    return equation, inputs


equation, inputs = textTolist('puzzle19test.txt')
equation, inputs = textTolist('puzzle19challenge.txt')
# print(equation)
# print(inputs)

RulesDict = {}
for condition_line in equation:
    nameCondtion, conditions = condition_line.split("{")
    conditions = conditions.replace("}", '')
    lastoption = conditions.split(',')[-1]
    matches = re.findall(r'(\w)([<>])(\d+):(\w+)', conditions)
    conditions = [(var, (op, int(value), label)) for var, op, value, label in matches]
    RulesDict[nameCondtion] = (conditions, lastoption)



def num_possible(ranges,code='in'):

    if code == "R":
        return 0
    if code == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product


    conditions,lastoption=RulesDict[code]

    total=0
    for key,(op,limit,output) in conditions:
        lo,hi=ranges[key]

        if op == "<":
            pass_range = (lo, min(limit - 1, hi))
            non_pass_range = (max(limit, lo), hi)
        else:
            pass_range = (max(limit + 1, lo), hi)
            non_pass_range = (lo, min(limit, hi))

        #make a new dict to go to the nextlevel
        newcopy=dict(ranges)
        newcopy[key]=pass_range
        total +=num_possible(newcopy,output)
        # update the dict in order to move to the 2 iteration
        ranges=dict(ranges)
        ranges[key]=non_pass_range
    #the ranges are suitable for the last option
    total+=num_possible(ranges,lastoption)

    return total

print(num_possible({key: (1, 4000) for key in "xmas"}))