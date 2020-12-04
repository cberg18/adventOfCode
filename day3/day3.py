data = [line.strip() for line in open(r"D:\Documents\git\adventOfCode\day3\input.txt", 'r')]

data.pop(0)
j = 3
treeCount = 0

for k in data:
    print(k)
    print(j)
    if k[j] == '#':
        treeCount += 1
        print('Tree @' + str(j))
    print('j: ' + str(j) )
    j = j + 3
    print('j: ' + str(j) )
    if j > len(k) - 2:
        j = j - len(k)

print(treeCount)

print(len(k))
