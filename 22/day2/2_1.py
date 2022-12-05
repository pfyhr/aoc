score = 0
with open('day2/input.txt') as file:
    lines = file.readlines()

    for line in lines:
        oppmove = 'null'
        usmove = 'null'
        for char in line:
            if char == 'A':
                oppmove = 'rock'
            elif char == 'B':
                oppmove = 'paper'
            elif char == 'C':
                oppmove = 'scissors'
            elif char == 'X':
                usmove = 'rock'
                score += 1
            elif char == 'Y':
                usmove = 'paper'
                score += 2
            elif char == 'Z':
                usmove = 'scissors'
                score += 3
            #else:
                #its a space or somesuch :)
        if oppmove == usmove:
            score += 3
        elif usmove == 'rock' and oppmove == 'scissors':
            score += 6
        elif usmove == 'paper' and oppmove == 'rock':
            score += 6
        elif usmove == 'scissors' and oppmove == 'paper':
            score += 6
        #else:
            #we dont care because we lost

print(score)


    