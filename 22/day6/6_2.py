with open('day6/input') as file:
    lines = file.readlines()
    line = lines[0]
    buffer = ''
    counter = 0
    for char in line:
        buffer +=char
        counter += 1
        if counter > 14:
            buffer = buffer[1:]
        nSame = 0
        for char in buffer:
            nSame += buffer.count(char)
        print(nSame)
        if nSame == 14:
            print('counter is: ', counter)
            break
        print(buffer, end='\n')

