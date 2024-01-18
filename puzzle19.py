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
#equation, inputs = textTolist('puzzle19challenge.txt')
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


# [print(key,'  ',value) for key,value in RulesDict.items()]

def partdictconstructor(iputline):
    partdict = {}
    matches = re.findall(r'(\w)(=)(\d+)', iputline)
    partdict = {var: int(val) for var, _, val in matches}
    return partdict


def part_tri(partinput):
    partstat = (partinput, 'in')
    while partstat[1] not in 'RA':
        partDict = partdictconstructor(partstat[0])
        (conditions, lastoption) = RulesDict[partstat[1]]
        eqresult = False
        for cond in conditions:
            var, eq = cond
            op, value, result = eq
            var = partDict[var]
            eqresult = (op == '>' and value < var) or (op == '<' and value > var)
            if eqresult:
                partstat = (partinput, result)
                break
        if not eqresult:
            partstat = (partinput, lastoption)
    return partDict, partstat[1]


total = 0
for ipt in inputs:
    partDict, result = part_tri(ipt)
    if result == 'A':
        total += sum(partDict.values())

print(total)







