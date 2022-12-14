def listsize(inlist):
    size = int(inlist[1])-int(inlist[0])
    return size

def splitline(line):
    splitline = line.split(',')  
    n1list = splitline[0].split('-')
    n2list = splitline[1].split('-')
    sizen1 = listsize(n1list)
    sizen2 = listsize(n2list)
    #returns in conditionals... ajajj
    if sizen1 > sizen2:
        return n1list, n2list
    else:
        return n2list, n1list

def contains(large, small):
    contains = 0
    if large[0] <= small[0] and large[1] >= small[1]:
        contains = 1
    #else nothing
    return contains

containpairs = 0
with open('day4/input.txt') as file:
    lines = file.readlines()

    for line in lines:
        #split line in 2, find largest set, see if it covers the smaller one
        large, small = splitline(line.strip())
        containpairs += contains(large, small)


print(containpairs)