# Advent of Code 2023 - Day 10

# ================ part I ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

direction = {
    "|": (( 1, 0),(-1, 0)),
    "-": (( 0, 1),( 0,-1)),
    "L": ((-1, 0),( 0, 1)),
    "J": ((-1, 0),( 0,-1)),
    "7": (( 1, 0),( 0,-1)),
    "F": (( 1, 0),( 0, 1)),
    ".": (),
    "S": (( 1, 0),(-1, 0),( 0, 1),( 0,-1))
}
w, h = len(t[0]), len(t)
start = None
dir_map = [[None for _ in range(w)] for _ in range(h)] # direction map

# find the possible direction from each tile
for i in range(h):
    for j in range(w):
        c = t[i][j]
        if c == "S": start = (i,j)
        direct = []
        for y,x in direction[c]:
            direct.append((i+y, j+x))
        dir_map[i][j] = direct

# remove impossible directions (ex: "7-" can not be connected)
for i in range(h):
    for j in range(w):
        vois = []
        for y,x in dir_map[i][j]:
            if 0<=x<w and 0<=y<h and (i,j) in dir_map[y][x]:
                vois.append((y,x))
        dir_map[i][j] = vois

# breadth-first search
depth_map = [[-1 for _ in range(w)] for _ in range(h)]
to_see = [start]
depth_map[start[0]][start[1]] = 0
max_depth = 0
while len(to_see) > 0:
    y,x = to_see.pop(0)
    for i,j in dir_map[y][x]:
        if depth_map[i][j] == -1:
            depth_map[i][j] = depth_map[y][x]+1
            to_see.append((i,j))
            max_depth = max(max_depth, depth_map[i][j])

print(f"part I: {max_depth}")

# ================ part II ================
"""
the code os very similar to part I
"""

t=[l.strip() for l in open('i.txt').readlines()]

direction = {
    "|": (( 1, 0),(-1, 0)),
    "-": (( 0, 1),( 0,-1)),
    "L": ((-1, 0),( 0, 1)),
    "J": ((-1, 0),( 0,-1)),
    "7": (( 1, 0),( 0,-1)),
    "F": (( 1, 0),( 0, 1)),
    ".": (),
    "S": (( 1, 0),(-1, 0),( 0, 1),( 0,-1))
}
w, h = len(t[0]), len(t)
start = None
dir_map = [[None for _ in range(w)] for _ in range(h)] # direction map
tile_map = [[t[i][j] for j in range(w)] for i in range(h)] # tile map

# find the possible direction from each tile
for i in range(h):
    for j in range(w):
        c = t[i][j]
        if c == "S": start = (i,j)
        direct = []
        for y,x in direction[c]:
            direct.append((i+y, j+x))
        dir_map[i][j] = direct

# remove impossible directions (ex: "7-" can not be connected)
for i in range(h):
    for j in range(w):
        vois = []
        for y,x in dir_map[i][j]:
            if 0<=x<w and 0<=y<h and (i,j) in dir_map[y][x]:
                vois.append((y,x))
        dir_map[i][j] = vois

# replace "S" with its corresponding tile
possib = ["|", "-", "L", "J", "7", "F"]
for y,x in dir_map[start[0]][start[1]]:
    new_possib = []
    for p in possib:
        if (y-start[0], x-start[1]) in direction[p]:
            new_possib.append(p)
    possib = new_possib
tile_map[start[0]][start[1]] = possib[0]

# depth-first search (to isolate the loop)
loop_map = [[" " for _ in range(w)] for _ in range(h)]
to_see = [start]
loop_map[start[0]][start[1]] = tile_map[start[0]][start[1]]
while len(to_see) > 0:
    y,x = to_see.pop()
    for i,j in dir_map[y][x]:
        if loop_map[i][j] == " ":
            loop_map[i][j] = tile_map[i][j]
            to_see.append((i,j))

# inside loop detection
"""
we use an horizontal ray to detect the number of loop edge (we ignore "-","F","7" - tangent problem)
- an even number of intersection means that we are outside
- an odd number of intersection means that we are inside
"""
temp_map = [[loop_map[i][j] for j in range(w)] for i in range(h)]
inside_tile = 0
for i in range(h):
    for j in range(w):
        if loop_map[i][j] == " ":
            pipe_count = 0
            for k in range(j+1, w):
                if loop_map[i][k] not in [" ","-","F","7"]:
                    pipe_count += 1

            inside_tile += pipe_count % 2 == 1  # the tile is inside if there is an odd number of intersection

print(f"part II: {inside_tile}")

