import sys
import numpy as np


# returns the union of two sets, whre a set is defined as the ones in a 2D grid
# output is the size of set1, set2 must be of same size
def intersect(set1, set2):
    length = len(set1)
    width = len(set1[0])
    if len(set2) != length or len(set2[0]) != width:
        print 'Error in Intersect: Sets do not match in size'
        return []
    grid = [[0 for x in range(width)] for y in range(length)] 
    for i in range(length):
        for j in range(width):
            if set1[i][j] == 1 and set2[i][j] == 1:
                grid[i][j] = 1
    return grid

# dilutes the basis with structuring element 
def dilute(basis, struct):
    length = len(basis)
    width = len(basis[0])
    grid = [[0 for x in range(width+len(struct[0])+2)] for y in range(length+len(struct)+2)] 
    for i in range(length):
        for j in range(width):
            if basis[i][j] == 1:
                for k in range(len(struct)):
                    grid[i+struct[k][0]+1][j+struct[k][1]+1] = 1 
    grid = [row [1:width+1] for row in grid[1:length+1]]
    return grid

# Retuns the 'first' hive from the total grid
def findHive(hiveGrid):
    hiveLength = len(hiveGrid)
    hive = [[0 for x in range(hiveLength)] for y in range(hiveLength)]
    # find the start of the hive
    for i in range(hiveLength):
        find = False
        for j in range(hiveLength):
            if hiveGrid[i][j] == 1:
                hive[i][j] = 1
                find = True
                break 
        if find:
            break
            
    # dilute untill the hive does not increase in size
    struct = [[int(-1),int(-1)],[int(-1),0],[int(-1),1],[0,int(-1)],[0,0],[0,1],[1,int(-1)],[1,0],[1,1]]
    hiveDilute = dilute(hive,struct)
    dilutedHive = intersect(hiveDilute,hiveGrid) 

    while dilutedHive != hive:
        hive = dilutedHive 
        hiveDilute = dilute(hive,struct)
        dilutedHive = intersect(hiveDilute,hiveGrid) 
    hive = dilutedHive
    return hive

def removeHive(hiveGrid, hive):
    # both parameters must be square and of same size
    for i in range(len(hiveGrid)):
        for j in range(len(hiveGrid[0])):
            hiveGrid[i][j] = hiveGrid[i][j] - hive[i][j]
    return hiveGrid

def findBiggestHive(hiveGrid):
    biggestHive = 0
    while np.sum(hiveGrid) != 0:
        hive = findHive(hiveGrid)
        hiveSum = np.sum(hive)
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

        
