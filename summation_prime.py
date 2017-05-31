primes = [2]
limit = 2000000
number = 2


while number < limit:
    if number%2 != 0:
        prime_counter = 0
        check_prime = number/2
        while check_prime > 1:
            if number%check_prime == 0:
                prime_counter += 1
                break
            check_prime -= 1

        if prime_counter == 0:
            print number
            primes.append(number)
    number += 1

print primes
print sum(primes)
