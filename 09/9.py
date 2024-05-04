# Advent of Code 2023 - Day 9 

# ================ part I ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

result = 0
for l in t:
    l = [int(k) for k in l.split()]
    stage = [l]
    while any(stage[-1]):
        new_stage = []
        for i in range(len(stage[-1])-1):
            new_stage.append(stage[-1][i+1]-stage[-1][i])
        stage.append(new_stage)

    k = 0
    n = len(stage)
    for i in range(n):
        k += stage[n-i-1][-1]
    result += k

print(f"part I: {result}")

# ================ part II ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

result = 0
for l in t:
    l = [int(k) for k in l.split()]
    stage = [l]
    while any(stage[-1]):
        new_stage = []
        for i in range(len(stage[-1])-1):
            new_stage.append(stage[-1][i+1]-stage[-1][i])
        stage.append(new_stage)

    k = 0
    n = len(stage)
    for i in range(n):
        k = stage[n-i-1][0]-k
    result += k

print(f"part II: {result}")

