# Advent of Code 2023 - Day 13

# ================ part I ================
"""
"""
import numpy as np

def partI():
    t=[list(l.strip()) for l in open('i.txt').readlines()]

    patterns = [[]]
    for l in t:
        if l == []: patterns.append([])
        else: patterns[-1].append(l)
    
    tot = 0
    idx = 0
    for p in patterns:
        w,h = len(p[0]), len(p)
        
        # we check if the twwo sides are the same
        temp = 0
        for c in range(w-1):
            reflect = True
            for i in range(w):
                if 0<=c-i<c+1+i<w:
                    for j in range(h):
                        if p[j][c-i] != p[j][c+1+i]:
                            reflect = False
            if reflect:
                temp += c+1

        for r in range(h-1):
            reflect = True
            for j in range(h):
                if 0<=r-j<r+1+j<h:
                    for i in range(w):
                        if p[r-j][i] != p[r+j+1][i]:
                            reflect = False
            if reflect:
                temp += 100*(r+1)

        tot += temp
        idx += 1

    return tot

print(f"part I: {partI()}")

# ================ part II ================
"""
"""

def partII():
    t=[list(l.strip()) for l in open('i.txt').readlines()]

    patterns = [[]]
    for l in t:
        if l == []: patterns.append([])
        else: patterns[-1].append(l)

    tot = 0
    idx = 0
    for p in patterns:
        w,h = len(p[0]), len(p)
        
        # we check if there is only one difference between the two sides
        temp = 0
        for c in range(w-1):
            diff = 0
            for i in range(w):
                if 0<=c-i<c+1+i<w:
                    for j in range(h):
                        if p[j][c-i] != p[j][c+1+i]:
                            diff += 1
            if diff == 1:
                temp += c+1

        for r in range(h-1):
            diff = 0
            for j in range(h):
                if 0<=r-j<r+1+j<h:
                    for i in range(w):
                        if p[r-j][i] != p[r+j+1][i]:
                            diff += 1
            if diff == 1:
                temp += 100*(r+1)

        tot += temp
        idx += 1

    return tot

print(f"part II: {partII()}")

