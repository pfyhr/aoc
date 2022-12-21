def makeBlocks(lines):
    blocks = [ [] for _ in range(9) ]
    
    for line in reversed(lines[0:8]):
        split = line.strip().split(' ')

        counter = 0
        while len(split)>9:
            for idx, item in enumerate(split):
                if idx < 8:
                    if split[idx] == '' and split[idx+1] == '':
                        split.pop(idx)
            
        
        # not nicely block printed... 
        # and way more work than it should have been
        for idx, thing in enumerate(split):
            if thing != '':
                #print(idx)
                blocks[idx].append(thing)
    print('starting state')
    printState(blocks)
    
    return blocks

def parseInstruction(line):
    split = line.strip().split(' ')
    #print(split)
    nr = int(split[1])
    fr = int(split[3])
    to = int(split[5])
    return nr, fr, to

def execInstruction(nr, fr, to):
    for n in range(nr):
        taken = blocks[fr-1].pop()
        blocks[to-1].append(taken)

def printState(blocks):
    for idx, line in enumerate(blocks):
        print(idx+1, ':', line)
    print('\n')

with open('day5/input.txt') as file:
    lines = file.readlines()

    blocks = makeBlocks(lines)

    #manual fudge
    execInstruction(1,9,6)
    execInstruction(1,4,3)
    print('we try again and start')
    printState(blocks)

    for line in lines[10:]:
        nr, fr, to = parseInstruction(line)
        execInstruction(nr, fr, to)
        printState(blocks)
    
    #extract the results!
    result = ''
    for thing in blocks:
        result += thing.pop().strip('[').strip(']')
    print('result is: ', result)
    