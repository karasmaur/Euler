import time
import json

before = time.time()

dict = {}
limit = 1000000

while limit > 1:
    number = limit
    count = 0
    while number > 1:
        if number % 2 == 0:
            number = int(number/2)
        else:
            number = int(3 * number + 1)
        count += 1
    dict[limit] = count
    limit -= 1

print(dict)

# Show elapse time:
print(before - time.time())

with open('data.json', 'w+') as fp:
    json.dump(dict, fp)