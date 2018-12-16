class Claim:
    def __init__(self, id, x,y,width,height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def getLinesFromInput():
    with open('input.txt') as f:
        return [line.rstrip() for line in f]

def parseClaim(claim):
        xStart = claim.find("@ ") + 2
        yStart = claim.find(",", xStart) + 1
        coOrdEnd = claim.find(":", yStart)
        dimensionSeparator = claim.find("x", coOrdEnd)

        return Claim(int(claim[1:xStart-3]),
                    int(claim[xStart:yStart - 1]),
                     int(claim[yStart: coOrdEnd]),
                    int(claim[coOrdEnd+2:dimensionSeparator]),
                     int(claim[dimensionSeparator+1:]) )
    
def getCounter(lines):
    cellClaims = []
    for claim in lines:
        c = parseClaim(claim)
        for w in range(c.x, c.x + c.width):
            for h in range(c.y, c.y + c.height):
                cellClaims.append( (w,h) )

    cellClaims.sort()
    from collections import Counter
    return Counter(cellClaims)

counter = getCounter(getLinesFromInput())
print(sum(1 for x in counter.values() if x > 1))