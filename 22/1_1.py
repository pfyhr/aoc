maxcal = 0
localsum = 0
with open('input.txt') as file:
    lines = file.readlines()

    for line in lines:
        if line.strip() == '':
            localsum = 0
        else:
            localsum += int(line.strip())
            if localsum > maxcal:
                maxcal = localsum

print(maxcal)