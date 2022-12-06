import string

def halveline(line):
    lineLength = len(line)
    chars1 = line[0:lineLength//2]
    chars2 = line[lineLength//2:]
    
    dupes = findcharin(chars1, chars2)
    return dupes

def findcharin(str1, str2):
    dupes = ''
    for char in str1:
        if (char in str2) and (char not in dupes):
            dupes += char
    return dupes

def ch2num(chin):
    letters = string.ascii_letters
    for i, ch in enumerate(letters):
        if ch == chin:
            retind = i
            break
    return retind+1

def numberify(dupeslist):
    val = 0
    for char in dupeslist:
        val += ch2num(char)
    return val


priosum = 0
with open('day3/input.txt') as file:
    lines = file.readlines()

    for line in lines:
        #split line in 2, find duplicates
        dupes = halveline(line)
        val = numberify(dupes)
        priosum += val

print(priosum)

