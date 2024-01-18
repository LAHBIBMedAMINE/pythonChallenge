

def textTolist(file_path):
    calibration = []
    with open(file_path, 'r') as file:
        for line in file:
            calibration.append(line.strip())
    return calibration



def findFirstandLastDigit(myString):
    firstDig = None
    lastDig = None

    for char in myString:
        if char.isdigit():
            if firstDig is None:
                firstDig = char
            lastDig = char

    if firstDig is not None:
        return int(firstDig + lastDig)
    else:
        return 0

file_path = "input.txt"
Calibration = textTolist(file_path)
total = 0
for word in Calibration:
    total = total + findFirstandLastDigit(word)

print("part1", total)


def FirstNumberLastNumber(mystring):
    mystring = mystring.lower()
    number_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for i in range(len(mystring)):
        for number_str, numeric_value in number_map.items():
            if i + len(number_str) <= len(mystring):
                if mystring[i:i + len(number_str)] == number_str:
                    mystring = mystring[:i] + numeric_value + mystring[i+1:]
    return findFirstandLastDigit(mystring)

test=textTolist("test.txt")
total2 = 0
for word in Calibration:
    'print(word, "==> ", FirstNumberLastNumber(word))'
    total2 = total2 + FirstNumberLastNumber(word)
print("part2", total2)







