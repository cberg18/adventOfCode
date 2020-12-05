def parse(next, step):
    data = [line.strip() for line in open(r"input.txt", 'r')]
    index = next
    data.pop(0)
    if step == 2:
        data.pop(0)
    treeCount = 0
    for k in range(0, len(data), step):
        #print(k)
        if data[k][index] == '#':
            treeCount += 1
        #print('index: ' + str(index))
        index = index + next
        #print('index: ' + str(index))
        if index > len(data[k]) - 2:
            index = index - len(data[k])
    return treeCount

print(parse(1, 1) * parse(3, 1) * parse(5, 1) * parse(7, 1) *
      parse(1, 2))
