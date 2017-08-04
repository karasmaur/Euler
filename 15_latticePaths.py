def createGrid(x, y):
    x, y = x + 2,  y + 2  # line and column
    grid = []
    for i in range(x):
        grid.append([])
        for j in range(y):
            if (i == 0 or j == 0) or (i + 1 == x or j + 1 == y):
                grid[i].append(False)
            else:
                grid[i].append(True)
    return grid

greed = createGrid(3, 3)
for line in greed:
    print(line)

for x in range(len(greed)):
    for y in range(len(greed)):


