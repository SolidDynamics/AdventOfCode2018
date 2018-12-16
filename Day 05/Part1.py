def reactPolymers(polymerString):
    excludeFromString = []

    skipNext = False
    for i in range(0,len(polymerString)-1):
        if skipNext:
            continue
        firstChar = str(polymerString[i])
        secondChar = str(polymerString[i+1])
        if(firstChar.lower() != secondChar.lower()):
            continue
        if(firstChar.islower != secondChar.islower):
            excludeFromString.append(i)
            excludeFromString.append(i+1)
            skipNext = True
    
    reducedPolymerString = ""
    for counter, c in enumerate(polymerString):
        if(counter not in excludeFromString):
            reducedPolymerString += c
            
    return reducedPolymerString

def getFullyReducedPolymerString(polymerString):
    while(True):
        reducedPolymerString = reactPolymers(polymerString)
        print(str(len(polymerString)) + "->" + str(len(reducedPolymerString)))
        if(len(polymerString) <= len(reducedPolymerString)):
            break
        polymerString = reducedPolymerString
    return polymerString

def getReducedPolymers(filename):
    with open(filename) as f:
        polymerString = f.read().splitlines()[0]

    print("Answer: " + str(len(getFullyReducedPolymerString(polymerString))))

if __name__ == "__main__":
    getReducedPolymers('sample.txt')
    getReducedPolymers('input.txt')