#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

sequence2 = [1, 2]
i = 0
while True:
    x = sequence2[i] + sequence2[i + 1]
    if len(str(x)) == 1000:
        print 'Fibonacci number: '+str(x)+'\r\n Index: '+str(i+4)
        break
    sequence2.append(x)
    i += 1
#print sequence2