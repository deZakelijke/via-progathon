import sys

def sum2(array):
    return sum(map(sum,array))

def index2(array):
    return [(ix,iy) for ix, row in enumerate(array) for iy, i in enumerate(row) if i== 1] 

# returns the union of two sets, whre a set is defined as the ones in a 2D grid
# output is the size of set1, set2 must be of same size
def intersect(set1, set2):
    length = len(set1)
    width = len(set1[0])
    grid = [[0 for x in range(width)] for y in range(length)] 
    for i in range(length):
        for j in range(width):
            if set1[i][j] == 1 and set2[i][j] == 1:
                grid[i][j] = 1
    return grid

# dilutes the basis with structuring element 
def dilute(basis):
    length = len(basis)
    width = len(basis[0])
    grid = [[0 for x in range(width+5)] for y in range(length+5)] 
    for i in range(length):
        for j in range(width):
            if basis[i][j] == 1:
                grid[i+2][j+2] = 1
                grid[i+2][j] = 1
                grid[i+2][j+1] = 1
                grid[i][j+2] = 1
                grid[i][j] = 1
                grid[i][j+1] = 1
                grid[i+1][j+2] = 1
                grid[i+1][j] = 1
                grid[i+1][j+1] = 1
    grid = [row [1:width+1] for row in grid[1:length+1]]
    return grid

# Retuns the 'first' hive from the total grid
def findHive(hiveGrid):
    hiveLength = len(hiveGrid)
    hive = [[0 for x in range(hiveLength)] for y in range(hiveLength)]
    # find the start of the hive
    startIndex = index2(hiveGrid)[0]
    hive[startIndex[0]][startIndex[1]] = 1
            
    # dilute untill the hive does not increase in size
    hiveDilute = dilute(hive)
    dilutedHive = intersect(hiveDilute,hiveGrid) 

    while dilutedHive != hive:
        hive = dilutedHive 
        hiveDilute = dilute(hive)
        dilutedHive = intersect(hiveDilute,hiveGrid) 
    hive = dilutedHive
    return hive

def removeHive(hiveGrid, hive):
    ones = index2(hive)
    for i in range(len(ones)):
        hiveGrid[ones[i][0]][ones[i][1]] = 0
    return hiveGrid

def findBiggestHive(hiveGrid):
    biggestHive = 0
    while sum2(hiveGrid) != 0:
        hive = findHive(hiveGrid)
        hiveSum = sum2(hive)
        if hiveSum > biggestHive:
            biggestHive = hiveSum
        hiveGrid = removeHive(hiveGrid, hive)

    return biggestHive


numberOfCases = int(raw_input())


for i in range(numberOfCases):
    # new beehive
    string = raw_input()
    if i != 0:
        print string
    beehive = []
    # first line is done by hand
    string = raw_input()
    beehive.append([])
    for k in range(len(string)):
        beehive[0].append(int(string[k]))
 
    for j in range(len(string)-1):
        string = raw_input()
        #new line in beehive
        beehive.append([])
        for k in range(len(string)):
            beehive[j+1].append(int(string[k]))
    
    biggestHive = findBiggestHive(beehive)    
    print biggestHive

        
