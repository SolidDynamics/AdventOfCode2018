f = open("input.txt", "r")
c = 0
for v in f:
    c = c + int(v)
print(c)