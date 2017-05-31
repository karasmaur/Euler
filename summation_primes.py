primes = 17
limit = 2000000
number = 8

import math
from time import time

start = time()

while number < limit:
    if number%2 != 0:
        if number%5 != 0:
            composite = False
            check_prime = 3
            prime_limit = math.sqrt(number)
            while check_prime <= prime_limit:
                if number%check_prime == 0:
                    composite = True
                    break
                check_prime += 2
            if not composite:
                #print number
                primes += number
    number += 1

elapsed = time() - start

print elapsed
print primes


