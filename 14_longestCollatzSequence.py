import time
import json

before = time.time()

dict = {}
limit = 1000000

while limit > 400000:
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

search = max(dict.values())
print(search)
for key, value in dict.items():
    if value == search:
        print(key)

# Show elapse time:
print(time.time() - before)

with open('data.json', 'w+') as fp:
    json.dump(dict, fp)