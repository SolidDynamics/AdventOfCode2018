def getGuardSleepMinutes(lines):
    from dateutil import parser

    class GuardEvent:
        def __init__(self, datetime, event):
            self.datetime = datetime
            self.event = event
        
    guardEvents = []
    for event in lines:
        dateString = event[event.find("[")+1:event.find("]")]
        guardEvents.append(GuardEvent(parser.parse(dateString),event[event.find("] ")+2:]))

    guardEvents.sort(key=lambda x: x.datetime, reverse=False)

    guardSleep = {}
    guardid = 0
    sleepMinute = 0
    for ev in guardEvents:
        if ev.event[:5] == "Guard":
            guardid = int(ev.event[ev.event.find("#")+1:ev.event.find(" ",ev.event.find("#"))])
        if ev.event[:5] == "falls":
            sleepMinute = ev.datetime.minute
        if ev.event[:5] == "wakes":
            if guardid not in guardSleep:
                guardSleep[guardid] = []
            for min in range(sleepMinute,ev.datetime.minute):
                guardSleep[guardid].append(min)
    return guardSleep

def getSleepiestGuardMinute(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    guardSleep = getGuardSleepMinutes(lines)
    sortedGuards = sorted(guardSleep, key=lambda k: len(guardSleep[k]), reverse=True)
    sleepiestGuard = sortedGuards[0]
    print("Sleepiest guard: " + str(sleepiestGuard))
    print("Sleepiest guard total minutes: " + str(len(guardSleep[sleepiestGuard])))

    from collections import Counter
    counter = Counter(guardSleep[sleepiestGuard])

    import operator
    sleepiestminute = max(counter.items(), key=operator.itemgetter(1))[0]

    print("Sleepiest minute of the sleepiest guard: " + str(sleepiestminute))
    print("Puzzle answer: " + str(sleepiestminute * sleepiestGuard))

if __name__ == "__main__":
    getSleepiestGuardMinute('sample.txt')
    getSleepiestGuardMinute('input.txt')  
