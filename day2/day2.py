data = [line.strip() for line in open(r"D:\Documents\git\adventOfCode\day2\input.txt", 'r')]

passing = []

def passcheck(password):
    policy = password.split(' ')[0].split('-')
    letter = password.split(' ')[1][0]
    password = password.split(' ')[2]

    count = 0
    if (password[int(policy[0])-1] == letter and password[int(policy[1])-1] != letter):
            passing.append(password)
            print('pass')
    elif (password[int(policy[0])-1] != letter and password[int(policy[1])-1] == letter):
            passing.append(password)
            print('pass')
    else:
        print('fail')


for i in range(len(data)):
    passcheck(data[i])


print(len(passing))
