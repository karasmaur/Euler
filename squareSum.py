
sumosquares = 0
for i in range(1,101):
    sumosquares += i**2
squareosums = 0
for i in range(1,101):
    squareosums += i
squareosums = squareosums**2
print sumosquares
print squareosums

print squareosums - sumosquares