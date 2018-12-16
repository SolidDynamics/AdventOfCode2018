f = open("input.txt", "r")
found = [0]
freq = 0
discovered = 0
while not discovered:
    f.seek(0)
    for input in f:
        freq = freq + int(input)
        if freq in found:
            discovered = 1
            break
        else:
            found.append(freq)
print(freq)