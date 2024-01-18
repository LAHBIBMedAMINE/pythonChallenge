print('(---------------------------------PartOne-----------------------------------------)')

print("step 1 convert file to dictionary key='AJ145':value='bit'")
def textTodict(file_path):
    handdictV = {}
    with open(file_path, 'r') as file:
        for line in file:
            handdictV[line.strip().split(" ")[0]] = int(line.strip().split(" ")[1])
    return handdictV


#file_path = 'puzzle7test.txt'
file_path = 'puzzle7challenge.txt'
handdictV = textTodict(file_path)


# print(handdictV)
def count_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    hand = list(char_count.items())
    if hand[0][1] == 5:
        return 6
    elif hand[0][1] == 4:
        return 5
    elif hand[0][1] == 3 and hand[1][1] == 2:
        return 4
    elif hand[0][1] == 3:
        return 3
    elif hand[0][1] == 2 and hand[1][1] == 2:
        return 2
    elif hand[0][1] == 2:
        return 1
    else:
        return 0


charorder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
charorder.reverse()
# print(charorder)

print("step 2 update the dict  key='AJ145':value=(card type,bit)")
for hand in list(handdictV.keys()):
    handdictV[hand] = (count_characters(hand), handdictV[hand])

handdictV = dict(sorted(handdictV.items(), key=lambda item: item[1][0], reverse=True))
# print(handdictV)

print("step 3 sort the hand by type 0 1 2 3 4 5 6")
print("       sort the hand by rule of first char")
hand = []
for v in sorted(list(set(v[0] for v in handdictV.values()))):
    handCat = [key for key, value in handdictV.items() if value[0] == v]
    if len(handCat) >= 2:
        opFlag = True
        while opFlag:
            opFlag = False
            for i in range(len(handCat) - 1):
                for char1, char2 in zip(handCat[i], handCat[i + 1]):
                    if charorder.index(char1) > charorder.index(char2):
                        sw = handCat[i]
                        handCat[i] = handCat[i + 1]
                        handCat[i + 1] = sw
                        opFlag = True
                        break
                    elif charorder.index(char1) < charorder.index(char2):
                        break

    hand.extend(handCat)
print("step 4 calculate the sum")
sum = 0
for r, h in enumerate(hand):
    sum += handdictV[h][1] * (r + 1)

print('total= ',sum)

print('(---------------------------------PartTwo-----------------------------------------)')
print("step 1 convert file to dictionary key='AJ145':value='bit'")

charorderJ = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
charorderJ.reverse()
# print(charorderJ)
handdictVJ = textTodict(file_path)

print("step 2 update the dict  key='AJ145':value=(card type,bit)")
def count_charactersJ(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    jokers = char_count.get('J', 0)
    hand_notJ = list(char_count.items())
    hand_notJ = [(key, value) for key, value in hand_notJ if key != 'J']
    if (not hand_notJ):
        return 6
    elif hand_notJ[0][1] + jokers == 5:
        return 6
    elif hand_notJ[0][1] + jokers == 4:
        return 5
    elif hand_notJ[0][1] + jokers == 3 and hand_notJ[1][1] == 2:
        return 4
    elif hand_notJ[0][1] + jokers == 3:
        return 3
    elif (hand_notJ[0][1] == 2) and (jokers or hand_notJ[1][1] == 2):
        return 2
    elif hand_notJ[0][1] == 2 or jokers:
        return 1
    else:
        return 0



for hand in list(handdictVJ.keys()):
    handdictVJ[hand] = (count_charactersJ(hand), handdictVJ[hand])

# print(handdictVJ)
handdictVJ = dict(sorted(handdictVJ.items(), key=lambda item: item[1][0], reverse=True))
# print(handdictVJ)

print("step 3 sort the hand by type 0 1 2 3 4 5 6")
print("       sort the hand by rule of first char")
hand = []
for v in sorted(list(set(v[0] for v in handdictVJ.values()))):
    handCat = [key for key, value in handdictVJ.items() if value[0] == v]
    if len(handCat) >= 2:
        opFlag = True
        while opFlag:
            opFlag = False
            for i in range(len(handCat) - 1):
                for char1, char2 in zip(handCat[i], handCat[i + 1]):
                    if charorderJ.index(char1) > charorderJ.index(char2):
                        sw = handCat[i]
                        handCat[i] = handCat[i + 1]
                        handCat[i + 1] = sw
                        opFlag = True
                        break
                    elif charorderJ.index(char1) < charorderJ.index(char2):
                        break

    hand.extend(handCat)

print("step 4 calculate the sum")
# print(hand)
sum = 0
for r, h in enumerate(hand):
    sum += handdictV[h][1] * (r + 1)

print('total= ',sum)
