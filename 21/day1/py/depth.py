import numpy as np

def windowSum(windowLength, data):
    movAvg = []
    for idx, value in enumerate(data[0:-(windowLength-1)]):
        wSum = sum(data[idx:idx+windowLength])
        movAvg.append(wSum)
    return movAvg

def part1(data):
    prevValue = data[0]
    resultList = []
    depthIncreases = 0
    for idx, value in enumerate(data[1:]):
        if value > prevValue:
            resultList.append(1)
            depthIncreases += 1
        else:
            resultList.append(0)
        prevValue = value

    print('increases =',depthIncreases)
    return(resultList)

#inputs
data = np.loadtxt('input.txt').astype(int)
windowLength=3

#solve part 1
reslist1 = part1(data)

#solve part 2
movAvg = windowSum(windowLength, data)
reslist2 = part1(movAvg)