# Advent of Code 2023 - Day 11

# ================ part I ================
"""
"""

t=[list(l.strip()) for l in open('i.txt').readlines()]

w, h = len(t[0]), len(t)

# find the colums and rows to duplicate
to_expend_col = [True for _ in range(w)]
to_expend_row = [True for _ in range(h)]
for i in range(h):
    for j in range(w):
        if t[i][j] == "#":
            to_expend_col[j] = False
            to_expend_row[i] = False

# expand the image (calculate the true position of each galaxy)
galaxy_pos, galaxy_id = {}, 0
x,y = 0,0
for i in range(h):
    x=0
    for j in range(h):
        if t[i][j] == "#":  # found galaxy
            galaxy_pos[galaxy_id] = (y,x)
            galaxy_id += 1

        if to_expend_col[j]: x += 2
        else: x += 1

    if to_expend_row[i]: y += 2
    else: y += 1


# calculate the sum of the lengths 
result = 0
for i in range(galaxy_id):
    for j in range(i+1, galaxy_id):
        dx = abs(galaxy_pos[i][1] - galaxy_pos[j][1])
        dy = abs(galaxy_pos[i][0] - galaxy_pos[j][0])
        result += dx+dy

print(f"part I: {result}")

# ================ part II ================
"""
exactly the same code as part I with 2->1000000
"""

t=[list(l.strip()) for l in open('i.txt').readlines()]

w, h = len(t[0]), len(t)

# find the colums and rows to duplicate
to_expend_col = [True for _ in range(w)]
to_expend_row = [True for _ in range(h)]
for i in range(h):
    for j in range(w):
        if t[i][j] == "#":
            to_expend_col[j] = False
            to_expend_row[i] = False

# expand the image (calculate the true position of each galaxy)
galaxy_pos, galaxy_id = {}, 0
x,y = 0,0
for i in range(h):
    x=0
    for j in range(h):
        if t[i][j] == "#":  # found galaxy
            galaxy_pos[galaxy_id] = (y,x)
            galaxy_id += 1

        if to_expend_col[j]: x += 1000000
        else: x += 1

    if to_expend_row[i]: y += 1000000
    else: y += 1


# calculate the sum of the lengths 
result = 0
for i in range(galaxy_id):
    for j in range(i+1, galaxy_id):
        dx = abs(galaxy_pos[i][1] - galaxy_pos[j][1])
        dy = abs(galaxy_pos[i][0] - galaxy_pos[j][0])
        result += dx+dy

print(f"part II: {result}")
