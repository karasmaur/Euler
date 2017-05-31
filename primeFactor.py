#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#In number theory, the prime factors of a positive integer are the prime numbers
# that divide that integer exactly.

# prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.

#  600.851.475.143
#   10000000000
#  300.425.737.571

thenumber = 600851475143

divisionControl = 2
if thenumber%2 == 0:
    if (thenumber/2)%2 != 0 and (thenumber/2)%3 != 0 and (thenumber/2)%5 != 0 and (thenumber/2)%7 != 0:
        print "this is it" + str(thenumber/2)
    divisionControl = 2
if thenumber%3 == 0:
    if (thenumber/3)%2 != 0 and (thenumber/3)%3 != 0 and (thenumber/3)%5 != 0 and (thenumber/3)%7 != 0:
        print "this is it" + str(thenumber/3)
    divisionControl = 3
if thenumber%5 == 0:
    if (thenumber/5)%2 != 0 and (thenumber/5)%3 != 0 and (thenumber/5)%5 != 0 and (thenumber/5)%7 != 0:
        print "this is it" + str(thenumber/5)
    divisionControl = 5
if thenumber%7 == 0:
    if (thenumber/7)%2 != 0 and (thenumber/7)%3 != 0 and (thenumber/7)%5 != 0 and (thenumber/7)%7 != 0:
        print "this is it" + str(thenumber/7)
    divisionControl = 7


i =  10000000000#the number divide by 2
while i < thenumber/divisionControl:
    if thenumber % i == 0:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print 'Largest Prime Factor' + str(i)
            break
    i += 1



