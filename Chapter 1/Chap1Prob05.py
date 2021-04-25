N = 50

for i in range (N):

    term = 0
    number = i

    while(number>0):
        term = term + number
        number -= 1

    print(i,term)