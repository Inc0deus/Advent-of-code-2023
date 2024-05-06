# Advent of Code 2023 - Day 18

# ================ part I ================
"""
"""

def partI():
    t=[l.strip() for l in open('i.txt').readlines()]
    plan = []
    for l in t:
        direct, dist, _ = l.split()
        plan.append((direct, int(dist)))
    
    min_r, max_r = float("inf"), float("-inf")
    min_c, max_c = float("inf"), float("-inf")
    trench_path = [(0,0)]
    r,c = 0,0
    for direct, dist in plan:
        for _ in range(dist):
            if direct == "U":
                r -= 1
                min_r = min(min_r, r)
            elif direct == "D":
                r += 1
                max_r = max(max_r, r)
            elif direct == "L":
                c -= 1
                min_c = min(min_c, c)
            elif direct == "R":
                c += 1
                max_c = max(max_c, c)
            trench_path.append((r,c))

    trench_map = []
    for i in range(max_r-min_r+1):
        row = []
        for j in range(max_c-min_c+1):
            if (i+min_r, j+min_c) in trench_path:
                row.append("#")
            else:
                row.append(".")
        trench_map.append(row)

    c = 0
    while c < len(trench_map[0]):
        if trench_map[0][c] == "#" and trench_map[1][c] == ".":
            break
        c += 1

    to_flood = [(1,c)]
    while to_flood != []:
        i,j = to_flood.pop()
        trench_map[i][j] = "#"
        if 0<=i+1<len(trench_map) and 0<=j<len(trench_map[0]) and trench_map[i+1][j] == ".": to_flood.append((i+1,j))
        if 0<=i-1<len(trench_map) and 0<=j<len(trench_map[0]) and trench_map[i-1][j] == ".": to_flood.append((i-1,j))
        if 0<=i<len(trench_map) and 0<=j+1<len(trench_map[0]) and trench_map[i][j+1] == ".": to_flood.append((i,j+1))
        if 0<=i<len(trench_map) and 0<=j-1<len(trench_map[0]) and trench_map[i][j-1] == ".": to_flood.append((i,j-1))

    space = 0
    for l in trench_map: space += l.count("#")

    return space

# print(f"part I: {partI()}")

# ================ part II ================
"""
https://www.youtube.com/@icub3d/videos
https://en.wikipedia.org/wiki/Shoelace_formula
"""

def partII():
    t=[l.strip() for l in open('i.txt').readlines()]

    plan = []
    for l in t:
        _, _, hexa = l.split()
        hexa = hexa[2:-1]
        direct = ["R", "D", "L", "U"][int(hexa[-1])]
        dist = int(hexa[:-1], 16)
        plan.append((direct, dist))

    min_r, max_r = float("inf"), float("-inf")
    min_c, max_c = float("inf"), float("-inf")
    trench_path = [(0,0)]
    r,c = 0,0
    ext = 0
    for direct, dist in plan:
        ext += dist/2
        if direct == "U":
            r -= dist
            min_r = min(min_r, r)
        elif direct == "D":
            r += dist
            max_r = max(max_r, r)
        elif direct == "L":
            c -= dist
            min_c = min(min_c, c)
        elif direct == "R":
            c += dist
            max_c = max(max_c, c)
        trench_path.append((r,c))
    ext += 1

    lace = 0
    for i in range(len(trench_path)-1):
        lace += (trench_path[i][1] * trench_path[i+1][0]) - (trench_path[i+1][1] * trench_path[i][0])

    A = int(ext + lace/2)
    return A

print(f"part II: {partII()}")
