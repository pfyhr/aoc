with open('day5/input.txt') as file:
    lines = file.readlines()

    instructions = [ [] for _ in range(9) ]
    for line in reversed(lines[0:8]):
        split = line.strip().split(' ')
        counter = 0
        for idx, item in enumerate(split):
            if item == '' and counter < 6:
                split.pop(idx)
                counter +=1
            else:
                counter = 0
        print(split)
        for idx, thing in enumerate(split):
            if thing != '':
                #print(idx)
                instructions[idx].append(thing)