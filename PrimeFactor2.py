thenumber = 600851475143
i = 8462696833
while i < thenumber/2:
    if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
        if thenumber%i == 0:
            print i
    i += 1