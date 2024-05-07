# Advent of Code 2023 - Day 21

# ================ part I ================
"""
"""

def partI():
    file = open('i.txt')

    garden = []
    start = None

    l = file.readline()
    idx = 0
    while l:
        l = list(l.strip())
        if "S" in l:
            start = (idx, l.index("S"))
        garden.append(l)

        l = file.readline()
        idx += 1

    R,C = len(garden), len(garden[0])

    def isValid(i, j):
        return 0 <= i < R and 0 <= j < C and garden[i][j] != "#"

    def nextPos(pos):
        next_pos = {}
        for i,j in pos:
            if isValid(i+1,j): next_pos[(i+1,j)] = None
            if isValid(i-1,j): next_pos[(i-1,j)] = None
            if isValid(i,j+1): next_pos[(i,j+1)] = None
            if isValid(i,j-1): next_pos[(i,j-1)] = None
        return next_pos

    pos = {start}
    for _ in range(64):
        pos = nextPos(pos)

    return len(pos)

print(f"part I: {partI()}")

# ================ part II ================
"""
https://blog.jverkamp.com/2023/12/21/aoc-2023-day-21-step-step-stepinator/#brute-force
https://stackoverflow.com/questions/19175037/determine-a-b-c-of-quadratic-equation-using-data-points
"""

def partII():
    file = open('i.txt')

    garden = []
    start = None

    l = file.readline()
    idx = 0
    while l:
        l = list(l.strip())
        if "S" in l:
            start = (idx, l.index("S"))
        garden.append(l)

        l = file.readline()
        idx += 1

    R,C = len(garden), len(garden[0])

    def quadCoefficient(x_1, y_1, x_2, y_2, x_3, y_3):
        a = y_1/((x_1-x_2)*(x_1-x_3)) + y_2/((x_2-x_1)*(x_2-x_3)) + y_3/((x_3-x_1)*(x_3-x_2))

        b = (-y_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
            -y_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
            -y_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

        c = (y_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
            +y_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
            +y_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

        return a,b,c

    def isValid(i, j):
        return garden[i%R][j%C] != "#"

    def nextPos(pos):
        next_pos = {}
        for i,j in pos:
            if isValid(i+1,j): next_pos[(i+1,j)] = None
            if isValid(i-1,j): next_pos[(i-1,j)] = None
            if isValid(i,j+1): next_pos[(i,j+1)] = None
            if isValid(i,j-1): next_pos[(i,j-1)] = None
        return next_pos

    nb_steps = 26501365
    half_cycle = (C-1)//2
    nb_cycles = (nb_steps-half_cycle)//C

    length = []
    pos = {start}
    i = 0
    while len(length) < 3:
        if (i-half_cycle)%C == 0:
            length.append(len(pos))

        pos = nextPos(pos)
        i += 1

    a,b,c = quadCoefficient(
        0, length[0],
        1, length[1],
        2, length[2]
    )
    
    return int(a*nb_cycles**2 + b*nb_cycles + c)

print(f"part II: {partII()}")

