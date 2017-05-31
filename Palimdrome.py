def checkPalim(number):
    number = str(number)
    check = 0

    length = len(number)

    for i in range(length/2):
        if number[i] == number[length-i-1]:
            check += 1

    if check == length/2:
        return True #print "IT'S A FUCKIN PALIMDROME"

x = 100
y = 100

pali = []

while x < 999:
    while y < 999:
        palia = x*y
        if checkPalim(palia):
            pali.append(palia)
        y += 1
    y = 100
    x += 1

print max(pali)
