# Advent of Code 2023 - Day 3

# ================ part I ================
"""
"""

t = [l.strip() for l in open('i.txt').readlines()]

result = 0
n = 0
check = False
for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j].isdigit():
            n = n*10 + int(t[i][j])
            for ii in [-1, 0, 1]:
                for jj in [-1, 0, 1]:
                    if 0<=i+ii<len(t) and 0<=j+jj<len(t[i]) and not t[i+ii][j+jj].isdigit() and t[i+ii][j+jj]!='.':
                        check = True
        elif n > 0:
            if check:
                result += n
            check = False
            n = 0

print(f"part I: {result}")

# ================ part II ================
"""
"""

t = [l.strip() for l in open('i.txt').readlines()]

# parse the text - find all the number and store them by their position
pos_num = {}
pos_same = {}
start_digit = None
n = 0
for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j].isdigit():
            if start_digit is None:
                start_digit = j
            n = n*10 + int(t[i][j])    
        if start_digit is not None and (j == len(t[i])-1 or not t[i][j].isdigit()):
            for k in range(j-start_digit):
                pos_same[(i, start_digit+k)] = []
                pos_num[(i, start_digit+k)] = n
                for l in range(j-start_digit):
                    pos_same[(i, start_digit+k)].append((i, start_digit+l))
            start_digit = None
            n = 0


result = 0
for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j] == "*":
            nb = []
            visited = {}
            for ii in [-1, 0, 1]:
                for jj in [-1, 0, 1]:
                    if (i+ii, j+jj) in pos_num and (i+ii, j+jj) not in visited:
                        nb.append(pos_num[(i+ii, j+jj)])
                        for same in pos_same[(i+ii, j+jj)]:
                            visited[same] = None

            if len(nb) == 2:
                result += nb[0]*nb[1]

print(f"part II: {result}")
