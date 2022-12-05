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
                usmove = 'lose'
                score += 0
            elif char == 'Y':
                usmove = 'draw'
                score += 3
            elif char == 'Z':
                usmove = 'win'
                score += 6
            #else:
                #its a space or somesuch :)
        if usmove == 'draw':
            usmove = oppmove
        elif usmove == 'win' and oppmove == 'scissors':
            usmove = 'rock'
        elif usmove == 'win' and oppmove == 'rock':
            usmove = 'paper'
        elif usmove == 'win' and oppmove == 'paper':
            usmove = 'scissors'
        elif usmove == 'lose' and oppmove == 'scissors':
            usmove = 'paper'
        elif usmove == 'lose' and oppmove == 'rock':
            usmove = 'scissors'
        elif usmove == 'lose' and oppmove == 'paper':
            usmove = 'rock'
        
        #score from play
        if usmove == 'rock':
            score += 1
        elif usmove == 'paper':
            score += 2
        elif usmove == 'scissors':
            score += 3

print(score)


    