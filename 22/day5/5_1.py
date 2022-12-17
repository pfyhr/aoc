from more_itertools import locate

with open('day5/input.txt') as file:
    lines = file.readlines()

    instructions = [ [] for _ in range(9) ]
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
        print(split) 
        for idx, thing in enumerate(split):
            if thing != '':
                #print(idx)
                instructions[idx].append(thing)