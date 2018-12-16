from Part1RecursionSolution import fullyReducePolymer 

def processFile(filename):
    with open(filename) as f:
        polymer = f.read().splitlines()[0]
    distinctChars = set(polymer.upper())
    results = {}
    for c in distinctChars:
        polymerRemovedChars = polymer.replace(c,'').replace(c.lower(),'')
        thisPolymer = fullyReducePolymer(polymerRemovedChars)
        results[c] = len(thisPolymer)
    
    print(results)
    lowestValue = min(results, key=results.get)
    print('Puzzle answer: ' + str(lowestValue) + " - " + str(results[lowestValue]))

if __name__ == "__main__":
    processFile('sample.txt')
    processFile('input.txt')