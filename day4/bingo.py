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

def marknumber(number, board, marks):
    for ridx, row in enumerate(board):
        for cidx, item in enumerate(row):
            if item == number:
                marks[ridx][cidx] = 1
    return marks



with open('day4/input.txt') as f:
    #lines = f.readlines()
    lines = [line.rstrip() for line in f]

input = lines[0]
#print(input)
# fake input here
input = [50, 98, 65, 14, 47]

skip = 2
rows = 5
board = [ ] #empty list of lists for board
marks = [ ]
boards = []    #list to hold boards
markboards = []

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
        marks.insert(row, [0 for num in line.split() if num.isdigit()])
        row += 1
        if row == 5:
            row = 0
            boards.append(board)
            markboards.append(marks)
            board = [ ]
            marks = [ ]
            skip = 1

print(boards[0])
print(boards[1])
print(markboards[0])

for number in input:
    for bidx, board in enumerate(boards):
        markedBoard = marknumber(number, board, markboards[bidx])
        markboards.insert(bidx, markedBoard)

print(markboards[0])

