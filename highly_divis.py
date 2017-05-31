import math

again = []
counter = 1
while True:
    sum_ = 0
    for n in range(1, counter):
        sum_ += n
    again.append(sum_)

    go = sum_/2
    divisor = 0

    for i in range(1, go):
        if go % i == 0:
            divisor += 1

    if divisor > 500:
        break

    counter += 1
print again
