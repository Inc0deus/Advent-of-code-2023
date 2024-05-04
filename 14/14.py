# Advent of Code 2023 - Day 14

# ================ part I ================
"""
"""

def partI():
    t=[list(l.strip()) for l in open('i.txt').readlines()]

    # sliding to the north
    for i in range(1, len(t)):
        for k in range(i, 0, -1):
            for j in range(len(t[0])):
                if t[k][j] == "O" and t[k-1][j] == ".":
                    t[  k][j] = "."
                    t[k-1][j] = "O"

    # calculate load
    load = 0
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == "O":
                load += len(t)-i
    
    return load

print(f"part I: {partI()}")

# ================ part II ================
"""
"""

from copy import deepcopy

def partII():
    t=[list(l.strip()) for l in open('i.txt').readlines()]

    def slideN(m):
        for i in range(1, len(m)):
            for k in range(i, 0, -1):
                for j in range(len(m[0])):
                    if m[k][j] == "O" and m[k-1][j] == ".":
                        m[  k][j] = "."
                        m[k-1][j] = "O"

    def slideS(m):
        for i in range(len(m)-2, -1, -1):
            for k in range(i, len(m)-1):
                for j in range(len(m[0])):
                    if m[k][j] == "O" and m[k+1][j] == ".":
                        m[  k][j] = "."
                        m[k+1][j] = "O"

    def slideW(m):
        for j in range(1, len(m[0])):
            for k in range(j, 0, -1):
                for i in range(len(m)):
                    if m[i][k] == "O" and m[i][k-1] == ".":
                        m[i][  k] = "."
                        m[i][k-1] = "O"

    def slideE(m):
        for j in range(len(m[0])-2, -1, -1):
            for k in range(j, len(m[0])-1):
                for i in range(len(m)):
                    if m[i][k] == "O" and m[i][k+1] == ".":
                        m[i][  k] = "."
                        m[i][k+1] = "O"

    def load(m):
        load = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == "O":
                    load += len(m)-i
        return load

    mem = []
    loop_s, loop_e = None, None
    N = 1000000000
    for i in range(1000000000):
        slideN(t)
        slideW(t)
        slideS(t)
        slideE(t)
        if t in mem:
            loop_s = mem.index(t)
            loop_e = i
            break

        mem.append(deepcopy(t))
    
    idx = (N-loop_s-1) % (loop_e - loop_s) + loop_s

    return load(mem[idx])

print(f"part II: {partII()}")

