#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10001st prime number?

primes = []#[2, 3, 5, 7]
number = 2

while True:
    m = number/2
    #print m
    anyDivisible = 0
    while m > 1:
        if number%m == 0:
            anyDivisible += 1
        m -= 1

    if anyDivisible == 0:
        primes.append(number)
    number += 1

    if len(primes) == 10001:
        break

print primes
print max(primes)
