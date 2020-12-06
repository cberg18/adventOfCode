data = [line.strip() for line in open(r"/home/cberg18/Documents/git/adventOfCode/day4/input.txt", 'r')]
reqFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
goodPass = []

def passCheck(password):
    password = ' '.join(password)
    password = password.split(':')
    password = ' '.join(password)
    password = password.split(' ')
    del password[1::2]
    #print(password)
    if 'cid' in password:
        password.remove('cid')
    check =  all(item in password for item in reqFields)
    if check == True:
        goodPass.append(1)


breaks = [0]
for i in range(len(data)):
    if data[i] == '':
        breaks.append(i)
breaks.append(len(data))

for i in range(len(breaks)):
    end = breaks[-1]
    if breaks[i] == end:
        break
    if i == 0:
        passCheck(data[breaks[i]:breaks[i+1]])
    else:
        passCheck(data[breaks[i]+1:breaks[i+1]])

print('There are ' + str(len(goodPass)) + ' valid passwords.')
