import time
before = time.time()

def divisor(number):
    limit = number
    divisions = 0
    i = 1

    if number == 1:
        return 1

    while limit > i:
        if limit % i == 0:
            limit = int(number / i)
            if limit != i:
                divisions += 1
            divisions += 1
        i += 1
    return divisions

print(divisor(28))

n = 1
while True:
    number = n * (n + 1) / 2
    if divisor(number) >= 500:
        print(number)
        break
    n += 1

print(time.time() - before)
