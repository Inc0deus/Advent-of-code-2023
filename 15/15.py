# Advent of Code 2023 - Day 15

# ================ part I ================
"""
"""

def partI():
    t = [l.strip() for l in open('i.txt').readlines()]
    t = "".join(t).split(",")

    def hash(s):
        v = 0
        for c in s:
            v += ord(c)
            v *= 17
            v %= 256
        return v

    tot = 0
    for s in t:
        tot += hash(s)

    return tot

print(f"part I: {partI()}")

# ================ part II ================
"""
"""

def partII():
    t = [l.strip() for l in open('i.txt').readlines()]
    t = "".join(t).split(",")

    def hash(s):
        v = 0
        for c in s:
            v += ord(c)
            v *= 17
            v %= 256
        return v

    boxes = [[] for _ in range(256)]
    focal = {}

    for op in t:
        if "=" in op:
            l, f = op.split("=")
            box = hash(l)
            if l in boxes[box]:
                focal[(box, l)] = int(f)
            else:
                boxes[box].append(l)
                focal[(box, l)] = int(f)
        elif "-" in op:
            l, _ = op.split("-")
            box = hash(l)
            if l in boxes[box]:
                del focal[(box, l)]
                del boxes[box][boxes[box].index(l)]

    power = 0
    for b in range(len(boxes)):
        for l in range(len(boxes[b])):
            power += (b+1)*(l+1)*focal[(b, boxes[b][l])]

    return power

print(f"part II: {partII()}")

