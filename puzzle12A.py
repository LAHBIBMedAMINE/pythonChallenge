def textToMatrix(file_path):
    sequence = []
    validsequence=[]
    with open(file_path, 'r') as file:
        for line in file:
            seq,vseq=line.strip().split(" ")
            sequence.append(seq)
            validsequence.append(vseq.split(","))
            validsequence = [[int(el) for el in element] for element in validsequence]
    return sequence,validsequence

sequence,validsequence=textToMatrix("puzzle12test.txt")
sequence,validsequence=textToMatrix("puzzle12challenge.txt")

def combo(sequence):
    if sequence=="":
        return [""]
    return [x+y for x in ('#.' if sequence[0]=='?' else sequence[0]) for y in combo(sequence[1:]) ]


total=0
for seq,Valseq in zip(sequence,validsequence):
    for combs in combo(seq):
        if Valseq == [len(block) for block in combs.split(".") if block]:
            total+=1


print(total)


