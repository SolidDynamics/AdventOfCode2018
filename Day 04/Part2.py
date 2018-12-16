from Part1 import getGuardSleepMinutes

def getSleepiestMinuteForGuard(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    guardSleep = getGuardSleepMinutes(lines)

    guardSleepByMinute = {} 
    for k,v in guardSleep.items():
        for minute in v:
            thisGuardMinute = (k, minute)
            if thisGuardMinute not in guardSleepByMinute:
                guardSleepByMinute[thisGuardMinute] = 0
            guardSleepByMinute[thisGuardMinute] += 1

    import operator
    mostSleepMinutes = max(guardSleepByMinute.items(), key=operator.itemgetter(1))[0]
    print("Guard:" + str(mostSleepMinutes[0]))
    print("Minute:" + str(mostSleepMinutes[1]))
    print("Freq:" + str(guardSleepByMinute[mostSleepMinutes]))
    
    print("Puzzle answer:" + str(mostSleepMinutes[0] * mostSleepMinutes[1]))

if __name__ == "__main__":
    getSleepiestMinuteForGuard('sample.txt')
    getSleepiestMinuteForGuard('input.txt')  
