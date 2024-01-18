import re


#file_path='puzzle5test.txt'
file_path='puzzle5challenge.txt'

def textToMatrix(file_path):
    with open(file_path, 'r') as file:
        puzzle_input = file.read()

    segments = puzzle_input.split('\n\n')
    maps=[]
    seeds = re.findall(r'\d+', segments[0])
    for seg in segments[1:]:
        maps.append(re.findall(r'(\d+) (\d+) (\d+)', seg))

    return seeds ,maps

seeds,maps=textToMatrix(file_path)

min_location = float('inf')
for seed in map(int,seeds):
    for mapi in maps:
        for seg in mapi:
            destination,source,delta = map(int,seg)
            if seed in range(source,source+delta):
                seed = (seed - source) + destination
                break
    min_location = min(seed, min_location)


print('partone= ',min_location)

'''
i=0
min_location = float('inf')
while i < len(seeds):
    for seed in range(int(seeds[i]),int(seeds[i]) +int(seeds[i+1])):
        for mapi in maps:
            for seg in mapi:
                destination, source, delta = map(int, seg)
                if seed in range(source, source + delta):
                    seed = (seed - source) + destination
                    break
        min_location = min(seed, min_location)
        i+=2

print(min_location)

'''

def chekinIntevals(maps, interval):
    x=interval[0]
    y=interval[1]
    level=interval[2]
    intervals=[]
    found=False
    for seg in maps[level-1]:
        destination,source,delta= map(int,seg)
        if source <= x < source + delta and y < source + delta:
            intervals.append((x - source + destination,y - source + destination,level+1))
            found = True
            break
        elif (x < source) and (source <= y < source + delta):
            intervals.append((x, source - 1, level))
            intervals.append((destination, y - source + destination, level + 1))
            found = True
            break

        elif (source <= x < source + delta) and (source + delta <= y):
            intervals.append((x - source + destination, destination+ delta-1, level + 1))
            intervals.append((source + delta, y, level))
            found = True
            break

        elif (x < source) and (y >= source + delta):
            intervals.append((x, source - 1, level))
            intervals.append((destination,destination+ delta-1, level+1))
            intervals.append((source + delta, y, level))
            found = True
            break

    if (not found):
        intervals.append((x, y, level+1))
    return intervals



min_location = float('inf')
for i in range(0, len(seeds), 2):
    x=int(seeds[i])
    y=int(seeds[i])+int(seeds[i+1])-1
    intervals = []
    intervals.append((x,y,1))


    while len(intervals) != 0:
        interval=intervals.pop()
        if (interval[2]<8):
            intervals.extend(chekinIntevals(maps,interval))
        else:
            min_location = min(interval[0], min_location)

print('parttwo= ',min_location)


