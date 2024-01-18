from collections import deque


def textTodict(file_path):
    nodedict = {}
    with open(file_path, 'r') as file:
        for line in file:
            trans, receiver = line.strip().split("->")
            receiver = receiver.split(',')
            receiver = [r.strip() for r in receiver]
            trans = trans.strip()

            if trans[0] == '%':
                nodedict[trans[1:]] = [trans[0], receiver, 0]
            elif trans[0] == '&':
                nodedict[trans[1:]] = [trans[0], receiver]
            else:
                nodedict[trans] = ['', receiver, '']

    for key, value in nodedict.items():
        cnxstat = {}
        if value[0] == '&':
            for k, v in nodedict.items():
                if key in v[1]:
                    cnxstat[k] = 'lo'
            nodedict[key].append(cnxstat)

    nodedict['button'] = 'broadcaster'
    return nodedict


nodedict = textTodict('puzzle20test1.txt')
nodedict= textTodict('puzzle20challenge.txt')
print(nodedict)


# print(inputs)

def flipflpfunction(sender, signal, receiver):
    if signal == 'lo':
        if nodedict[sender][2] == 0:
            return 'hi'
        if nodedict[sender][2] == 1:
            return 'lo'
    else:
        return None


def conjuction(sender, signal, receiver):
    nodedict[receiver][2][sender] = signal
    if all(value == 'hi' for value in nodedict[receiver][2].values()):
        return 'lo'
    else:
        return 'hi'


def transmitting(sender='elv', signal='lo', receivcnx='button'):
    output = []
    if receivcnx == 'button':
        output.append(('button', signal, 'broadcaster'))
    elif receivcnx == 'broadcaster':
        for cnx in nodedict['broadcaster'][1]:
            output.append(('broadcaster', signal, cnx))
    elif receivcnx in nodedict.keys():
        if nodedict[receivcnx][0] == '%':
            for cnx in nodedict[receivcnx][1]:
                output.append((receivcnx, flipflpfunction(receivcnx, signal, cnx), cnx))
            if signal == 'lo':
                nodedict[receivcnx][2] ^= 1
        elif nodedict[receivcnx][0] == '&':
            for cnx in nodedict[receivcnx][1]:
                output.append((receivcnx, conjuction(sender, signal, receivcnx), cnx))

    return output


num_lo = 0
num_hi = 0
for i in range(1000):
    output = deque()
    output.extend(transmitting())
    while output:
        if output:
            sender, signal, reciver = output.popleft()
            if (signal,reciver) == ('lo','rx'):
                print(i)
            #print(sender, signal, reciver)
        if signal is not None:
            if signal == 'lo':
                num_lo += 1
            else:
                num_hi += 1

            output.extend(transmitting(sender, signal, reciver))


print(num_lo* num_hi)
