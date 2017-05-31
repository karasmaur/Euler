
a = 0
b = 1
c = 2
pytha = 0

while a < 1000:
    a += 1
    while b < 1000:
        b += 1
        while c < 1000:
            c += 1
            if a**2 + b**2 == c**2:
                if a + b + c == 1000:
                    print 'A = ' + str(a) + ' - B = ' + str(b) + ' - C = ' + str(c)
                    pytha = a*b*c
                    break
        if pytha > 0:
            break
        c = b + 1
    if pytha > 0:
        break
    b = a + 1


print pytha

'''
A = 200**2 = 40000
B = 375**2 = 140625
C = 425**2 = 180625

'''