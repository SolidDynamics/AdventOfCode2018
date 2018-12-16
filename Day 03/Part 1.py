def GetCounter():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    cellClaims = []
    for claim in lines:
        xStart = claim.find("@ ") + 2
        yStart = claim.find(",", xStart) + 1
        coOrdEnd = claim.find(":", yStart)
        dimensionSeparator = claim.find("x", coOrdEnd)

        x = int(claim[xStart:yStart - 1])
        y = int(claim[yStart: coOrdEnd])
        width = int(claim[coOrdEnd+2:dimensionSeparator])
        height = int(claim[dimensionSeparator+1:])

        for w in range(x, x+width):
            for h in range(y, y+height):
                cellClaims.append( (w,h) )

    cellClaims.sort()
    from collections import Counter
    return Counter(cellClaims)

counter = GetCounter()
print(sum(1 for x in counter.values() if x > 1))