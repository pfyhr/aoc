def checkrows(board):
    counter = 0
    for idx, row in enumerate(board):
        print(row)
        for item in row:

            counter += item
        if counter == 5:
            return idx
        else:
            counter = 0
    return 'nothing'

with open('day4/input.txt') as f:
    #lines = f.readlines()
    lines = [line.rstrip() for line in f]

input = lines[0]
#print(input)

skip = 2
rows = 5
board = [ ] #empty list of lists for board
boards = []    #list to hold boards

#boards.append(board)
#boards.append(board)

def testCheckrows(board):
    board[2][:] = [1 for i in range(rows) ]

    print(board)
    print(checkrows(board))

#print(boards)

row = 0
for idx, line in enumerate(lines):
    if skip:
        skip -= 1
    else:
        #print(f'idx={idx}')
        board.insert(row, [int(num) for num in line.split() if num.isdigit()])
        row += 1
        if row == 5:
            row = 0
            boards.append(board)
            board = [ ]
            skip = 1

print(boards[0])
print(boards[1])