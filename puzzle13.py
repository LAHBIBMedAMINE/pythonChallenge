def textTolist(file_path):
    with open(file_path, 'r') as file:
        grid = file.read()
        grid = grid.split('\n\n')
        # [print(block) for block in grid]

    mylist = []
    for block in grid:
        rows = []
        block = block.split('\n')
        for line in block:
            rows.append([char for char in line.strip()])
        mylist.append(rows)

    return mylist


grid = textTolist('puzzle13test.txt')
grid = textTolist('puzzle13challenge.txt')
total = 0
for gd in grid:
    rows = gd
    columns = [[r[c] for r in rows] for c in range(len(rows[0]))]

    for r in range(1, len(rows)):
        downside = rows[r:]
        upperside = rows[:r][::-1]
        downside = downside[:len(upperside)]
        upperside = upperside[:len(downside)]

        if (upperside == downside):
            total += r * 100

    for c in range(1, len(columns)):
        rightside = columns[c:]
        leftside = columns[:c][::-1]
        rightside = rightside[:len(leftside)]
        leftside = leftside[:len(rightside)]

        if (leftside == rightside):
            total += c

print(total)

total = 0
for gd in grid:
    rows = gd
    columns = [[r[c] for r in rows] for c in range(len(rows[0]))]

    for r in range(1, len(rows)):
        downside = rows[r:]
        upperside = rows[:r][::-1]
        downside = downside[:len(upperside)]
        upperside = upperside[:len(downside)]

        mismatch = 0
        for rowx, rowy in zip(downside, upperside):
            for charx, chary in zip(rowx, rowy):
                if (charx != chary):
                    mismatch += 1

        if mismatch == 1:
            total += r*100

    for c in range(1, len(columns)):
        rightside = columns[c:]
        leftside = columns[:c][::-1]
        rightside = rightside[:len(leftside)]
        leftside = leftside[:len(rightside)]

        mismatch = 0
        for colx, coly in zip(rightside, leftside):
            for charx, chary in zip(colx, coly):
                if (charx != chary):
                    mismatch += 1

        if mismatch == 1:
            total += c

print(total)
