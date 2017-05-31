#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

sequence2 = [1, 2]
i = 0
while True:
    x = sequence2[i] + sequence2[i + 1]
    if x > 4000000:
        break
    sequence2.append(x)
    i += 1

soma = 0
for i in sequence2:
    if i%2 == 0:
        soma += i

print 'TOTAL: ' + str(soma)