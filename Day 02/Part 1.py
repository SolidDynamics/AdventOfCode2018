f = open("input.txt", "r")
codesWithTwo = 0
codesWithThree = 0
for code in f:
    letterDict = {}
    for c in code:
        if(c == "\n"):
            break
        if c in letterDict:
            letterDict[c] = letterDict[c] + 1
        else:
            letterDict[c] = 1
    hasTwo = 0
    hasThree = 0
    for count in letterDict:
        if(letterDict[count] == 2):
            hasTwo = 1
        if(letterDict[count] == 3):
            hasThree = 1
    if(hasTwo):
        codesWithTwo = codesWithTwo + 1
    if(hasThree):
        codesWithThree = codesWithThree + 1

print(codesWithThree * codesWithTwo)