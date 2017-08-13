f = open('grid', 'r');

lines = [];
for line in f:
    lines.append(line.replace("\n", ""));
f.close();

grid = [[0 for x in range(len(lines))] for y in range(0, len(lines[0]), 3)];

for i in range(len(lines)):
    k = 0;
    for j in range(0, len(lines[0]), 3):
       grid[i][k] = int(lines[i][j:j+2]);
       k += 1;

trueMax = 0;


def directionMax(x, y, ns, ew, grid):
    localMax = 0
    while x + 3*ns < len(grid[0]) and x + 3*ns >= 0 and y + 3*ew < len(grid) and y +  3*ew >= 0:
        product = grid[x][y]*grid[x + ns][y + ew] * grid[x + 2*ns][y + 2*ew] * grid[x + 3*ns][y + 3*ew];
        if product > localMax:
            localMax = product;
        x += ns;
        y += ew;
    return int(localMax);

dmax = 0;

for i in range(len(grid[0])):
    if i < len(grid[0]) - 3:
        dmax = directionMax(i, 0, 1, 1, grid);
        if trueMax < dmax:
            trueMax = dmax;
            
    if i > 3:
        dmax = directionMax(i, 0, -1, 1, grid);
        if trueMax < dmax:
            trueMax = dmax;
            
    dmax = directionMax(i, 0, 0, 1, grid);
    if trueMax < dmax:
        trueMax = dmax;


for j in range(len(grid)):
    if j < len(grid) - 3:
        dmax = directionMax(0, j, 1, 1, grid);
        if trueMax < dmax:
            trueMax = dmax;
            
    if i > 3:
        dmax = directionMax(0, j, 1, -1, grid);
        if trueMax < dmax:
            trueMax = dmax;
            
    dmax = directionMax(0, j, 0, 1, grid);
    if trueMax < dmax:
        trueMax = dmax;

print "Maximum produce: %i" % trueMax;
