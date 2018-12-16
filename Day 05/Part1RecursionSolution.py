# Model solution downloaded from https://www.reddit.com/r/adventofcode/comments/a3q03b/aoc_2018_day_5_divide_and_conquer_python/

with open('input.txt') as f:
    polymer = f.read()

def reactUnits(first, second):
    return first!=second and first.upper() == second.upper()

#divide and conquer solution
def react(polymer):
    L = len(polymer)
    if L == 1 or L == 0:
        return polymer
    elif L == 2:
        if reactUnits(polymer[0],polymer[1]):
            return ''
        else:
            return polymer
    else:
        cut = L//2
        if reactUnits(polymer[cut-1],polymer[cut]): 
            return combine(react(polymer[:cut-1]), react(polymer[cut+1:]))
        else:
            return combine(react(polymer[:cut]), react(polymer[cut:]))

def combine(a,b):
    if a == '' or b == '':
        return a + b
    elif a[-1] != b[0] and a[-1].upper() == b[0].upper():
        return combine(a[:-1], b[1:])
    else:
        return a + b

def fullyReducePolymer(polymer):
    import sys
    lim = sys.getrecursionlimit()
    sys.setrecursionlimit(3000)
    reducedPolymer = react(polymer)
    sys.setrecursionlimit(lim)
    return reducedPolymer
    
def processFile(filename):
    with open(filename) as f:
        polymer = f.read().splitlines()[0]
    product = fullyReducePolymer(polymer)
    print('Number of units remaining in '+ filename +': {}'.format(len(product)))

if __name__ == "__main__":
    processFile('sample.txt')
    processFile('input.txt')