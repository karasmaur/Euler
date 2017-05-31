j = 20
check = 0
while True:
    for i in range(1,21):
        if j%i == 0:
            check += 1
    if check == 20:
        print j
        break
    check = 0
    j += 1
