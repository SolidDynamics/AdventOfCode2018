def getDiffs(first = [], second = []):
    charcount = 0
    diff = []
    for l in first:
        if l != second[charcount]:
           diff.append(charcount)
        charcount += 1
    return diff

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

from itertools import combinations
for pair in list(combinations(lines,2)):
    diffs = getDiffs(pair[0], pair[1])
    if len(diffs) == 1:
        commonLetters = ""
        for counter, s in enumerate(pair[0]):
            if counter != diffs[0]:
                commonLetters += pair[0][counter]
        print(commonLetters)
        break