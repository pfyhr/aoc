import string



def findcharin(str1, str2):
    dupes = ''
    for char in str1:
        if (char in str2) and (char not in dupes):
            dupes += char
    return dupes

def ch2num(chin):
    letters = string.ascii_letters
    retind = -1
    for i, ch in enumerate(letters):
        if ch == chin:
            retind = i
            break
    return retind+1 #the enumerate indices start at 0...

def numberify(dupeslist):
    val = 0
    for char in dupeslist:
        val += ch2num(char)
    return val


priosum = 0
with open('day3/input.txt') as file:
    lines = file.readlines()

    grplinecount = 0
    oldline = ''
    dupes = ''
    for line in lines:
        #compare first line w 2nd, find intersection
        #then compare intersection w 3rd line.
        grplinecount += 1
        if grplinecount%2 == 0:
            dupes = findcharin(oldline, line)
        elif grplinecount%3 == 0:
            badge = findcharin(dupes, line)
            print(badge)
            val = numberify(badge)
            priosum += val
            dupes = ''       #set these to blank to reset the grp count thing
            oldline = ''     #also this
            grplinecount = 0 #also this
        else:
            oldline = line

            
        

print(priosum)

