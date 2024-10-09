from arrays import Array

def fileToArray(inFileName):
    inFile = open(inFileName, "r")
    aList = []

    for line in inFile:
        line.rstrip()
        aList = line.split()
    
    inFile.close()
    
    arr = Array(len(aList))

    for i in range(len(aList)):
        arr[i] = aList[i]

    return arr