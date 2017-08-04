file = open('13_input.txt').readlines()
print(str(sum([int(line) for line in file]))[0:10])

