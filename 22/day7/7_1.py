with open('day7/input') as file:
    lines = file.readlines()
    
    #init some useful stuff
    maxsize = 100000
    curloc = '/'
    fs = {}

    for line in lines:
        if line[0] == '$'
            if line[2:3] == 'cd':
                if line[5] == '/':
                    curloc = '/'
                elif line[5:6] == '..':
                    #curloc, split / take away last, put back together.
                    #set curloc
                else:
                    curlock += line[5:] 
            elif line[2:3] == 'ls':
                #ignore and wait for output of the ls   
        else:
            cut = line.split(' ')
            fs.append({ "f{cut[1]}" : cut[0] )
            

    