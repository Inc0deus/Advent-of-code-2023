# Advent of Code 2023 - Day 2

# ================ part I ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

game = []
for l in t:
    l = l.split(":")[1].split(";")
    subsets = []
    for p in l:
        s = {}
        p = p.split(",")
        for t in p:
            t = t.split()
            s[t[1]] = int(t[0])
        subsets.append(s)
    game.append(subsets)

maxi = {"red": 12, "green": 13, "blue": 14}
result = 0
for i in range(len(game)):
    for sub in game[i]:
        check = False
        for m in maxi:
            check |= m in sub and sub[m]>maxi[m]
        if check:
            break
    else:
        result += i+1

print(f"part I: {result}")

# ================ part II ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

game = []
for l in t:
    l = l.split(":")[1].split(";")
    subsets = []
    for p in l:
        s = {}
        p = p.split(",")
        for t in p:
            t = t.split()
            s[t[1]] = int(t[0])
        subsets.append(s)
    game.append(subsets)

result = 0
for i in range(len(game)):
    r,g,b = 0,0,0
    for sub in game[i]:
        if "red" in sub and sub["red"] > r: r=sub["red"]
        if "green" in sub and sub["green"] > g: g=sub["green"]
        if "blue" in sub and sub["blue"] > b: b=sub["blue"]

    result += r*g*b
        

print(f"part II: {result}")

