from Part1 import getCounter, getLinesFromInput, parseClaim
lines = getLinesFromInput()
counter = getCounter(lines)

for claim in lines:
    c = parseClaim(claim)
    multipleClaims = False
    for w in range(c.x, c.x + c.width):
        for h in range(c.y, c.y + c.height):
            if counter[(w,h)] > 1:
                multipleClaims = True
                break
        if multipleClaims:
            break
    if multipleClaims:
        continue
    print(c.id)
    break