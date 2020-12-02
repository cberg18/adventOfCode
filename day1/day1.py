data = [int(line.strip()) for line in open("/home/cberg18/Documents/git/adventOfCode/day1/input.txt", 'r')]

def check(input):
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i*j*k

print(check(data))
