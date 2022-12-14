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
    if sizen1 >= sizen2:
        return n1list, n2list
    else:
        return n2list, n1list

def intersect(large, small):
    intersect = 0
    for n in range(int(small[0]),(int(small[1])+1)):
        if n == int(large[0]) or n == int(large[1]):
            intersect = 1
    #else nothing
    return intersect

def contains(large, small):
    contains = 0
    if (int(large[0]) <= int(small[0])) and \
        (int(large[1]) >= int(small[1])):
        contains = 1
    #else nothing
    return contains

containpairs = 0
with open('day4/input.txt') as file:
    lines = file.readlines()

    for line in lines:
        #split line in 2, find intersections in set 
        large, small = splitline(line.strip())
        if contains(large, small) != 0 or intersect(large,small) != 0:
            containpairs += 1


print(containpairs)