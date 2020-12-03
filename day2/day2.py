data = [line.strip() for line in open(r"D:\Documents\git\adventOfCode\day2\input.txt", 'r')]

passing = []

def passcheck(password):
    policy = password.split(' ')[0]
    letter = password.split(' ')[1][0]
    password = password.split(' ')[2]

    policy = policy.split('-')


    count = 0
    for i in range(len(password)):
        #print('password: ' + password[i] + ' Letter: ' + letter)
        if password[i] == letter:
            count += 1

    if count >= int(policy[0]) and count <= int(policy[1]):
        print('pass')
        passing.append(password)
    else:
        print('fail')


for i in range(len(data)):
    passcheck(data[i])


print(len(passing))
