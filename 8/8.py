# Advent of Code 2023 - Day 8

# ================ part I ================
"""
"""

t = [l.strip() for l in open('i.txt').readlines()]

instr = t[0]
n = len(instr)
L, R = {}, {}
for l in t[2:]:
    l = l.split(" = ")
    node = l[0]
    left,right = l[1].replace("(","").replace(")","").split(", ")
    L[node], R[node] = left, right

node = "AAA"
i = 0
while node != "ZZZ":
    if instr[i%n] == "L":
        node = L[node]
    else:
        node = R[node]
    i += 1

result = i

print(f"part I: {result}")

# ================ part II ================
"""
"""

from math import sqrt

def decomp(n):
    d = {}
    if n==1:
        return d

    while n>=2:
        x,r = n//2,n%2
        if r!=0: break
        n = x

        if 2 not in d: d[2] = 1
        else: d[2] += 1

    i=3
    rn = sqrt(n)+1
    while i<=n:
        if i>rn:
            if n not in d: d[n] = 1
            else: d[n] += 1
            break
        x,r = n//i,n%i
        if r==0:
            if i not in d: d[i] = 1
            else: d[i] += 1
            n=x
            rn=sqrt(n)+1
        else:
            i+=2
    return d

def _lcm(x1, x2):   # lowest common multiple
    d1, d2 = decomp(x1), decomp(x2)
    r = 1

    seen = {}
    for k in d1:
        if k in d2:
            r *= k ** max(d1[k], d2[k])
        else:
            r *= k ** d1[k]
        seen[k] = None
    for k in d2:
        if k not in seen:
            if k in d1:
                r *= k ** max(d1[k], d2[k])
            else:
                r *= k ** d2[k]
    return r

def lcm(*val):
    if len(val) == 2:
        return _lcm(val[0], val[1])
    return lcm(_lcm(val[0], val[1]), *val[2:])

t=[l.strip() for l in open('i.txt').readlines()]

instr = t[0]
n = len(instr)
L, R = {}, {}
nodes = []
end_with_z = []
for l in t[2:]:
    l = l.split(" = ")
    node = l[0]
    left,right = l[1].replace("(","").replace(")","").split(", ")
    L[node], R[node] = left, right
    if node[-1] == "A":
        nodes.append(node)
        end_with_z.append(False)

nb_end = []
for k in range(len(nodes)):
    i = 0
    while not end_with_z[k]:
        if instr[i%n] == "L":
            nodes[k] = L[nodes[k]]
        else:
            nodes[k] = R[nodes[k]]

        if nodes[k][-1] == "Z": end_with_z[k] = True
        else: end_with_z[k] = False
        i += 1
    nb_end.append(i)

result = lcm(*nb_end)

print(f"part II: {result}")
