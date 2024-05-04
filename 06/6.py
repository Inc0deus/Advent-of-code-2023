# Advent of Code 2023 - Day 6

# ================ part I ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]
rec_time = [int(l) for l in t[0].replace("Time:", "").split()]
rec_dist = [int(l) for l in t[1].replace("Distance:", "").split()]

result = 1
for i in range(len(rec_time)):
    t,d = rec_time[i],rec_dist[i]

    ways = 0
    for i in range(t+1):
        if i * (t-i) > d: ways += 1
    result *= ways

print(f"part I: {result}")

# ================ part II ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]
rec_time = int("".join([l for l in t[0].replace("Time:", "").split()]))
rec_dist = int("".join([l for l in t[1].replace("Distance:", "").split()]))

result = 0
for i in range(rec_time):
    print(i, rec_time)
    if i * (rec_time-i) > rec_dist: result += 1

print(f"part II: {result}")

