maxcal = 0
localsum = 0
elvecals = []
with open('input.txt') as file:
    lines = file.readlines()

    for line in lines:
        if line.strip() == '':
            elvecals.append(localsum)
            localsum = 0
        else:
            localsum += int(line.strip())
            if localsum > maxcal:
                maxcal = localsum
elvecals.sort()
top3cals = sum(elvecals[-3:])
print(top3cals)