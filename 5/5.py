# Advent of Code 2023 - Day 5

# ================ part I ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

seeds = [int(s) for s in t[0].split()[1:]]

map = {}
values = {}
i = 2
while i < len(t):
    l = t[i]
    l = l.strip()
    if l != "":
        l = l.replace(" map:", "").split("-to-")
        map[l[0]] = l[1]
        values[l[1]] = []
        i += 1
        while i < len(t) and len(t[i]) > 0 and t[i][0].isdigit():
            dest, sour, rang = (int(m) for m in t[i].split())
            values[l[1]].append((dest, sour, rang))
            i += 1
    i += 1

result = float("inf")
for s in seeds:
    cat = "seed"
    val = s
    while cat != "location":
        cat = map[cat]
        for dest, sour, rang in values[cat]:
            if sour <= val <= sour+rang-1:
                val = dest+(val-sour)
                break
    if val < result:
        result = val

print(f"part I: {result}")

# ================ part II ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]
seeds = [int(s) for s in t[0].split()[1:]]

# tokenize the file
map = {}            # {x:y} -> x-to-y
values = {}         # each line of values tokenized
source_range = {}   # range of the source
i = 2
while i < len(t):
    l = t[i]
    if l != "":
        l = l.replace(" map:", "").split("-to-")
        map[l[0]] = l[1]
        values[l[1]] = []
        v = []
        i += 1
        j = 0
        while i < len(t) and len(t[i]) > 0 and t[i][0].isdigit():
            dest, sour, rang = (int(m) for m in t[i].split())
            values[l[1]].append((dest, sour, rang))
            v.append((sour,sour+rang-1,j))
            i += 1
            j += 1
        v.sort(key=lambda x:x[0])
        source_range[l[1]] = v
    i += 1

def convert_range(start_, end_, source):
    sub = []
    start = start_
    end = end_
    i = 0
    # cut the range in sub ranges made with the ranges available
    while start < end:
        if i < len(source_range[source]):
            s,e,id = source_range[source][i]
            if e >= start:
                if s > start:
                    sub.append([start, min(e,end), None])
                    start = min(e,end)
                elif e >= end:
                    sub.append([start, end, id])
                    break
                elif e < end:
                    sub.append([start, e, id])
                    start = e+1
            i += 1
        else:
            sub.append([start, end, None])
            start = end

    # convert from source range to destination range (with the id of the couple dest-sour)
    for i in range(len(sub)):
        if sub[i][-1] is not None:
            dest, sour, rang = values[source][sub[i][-1]]
            sub[i][0] += dest-sour
            sub[i][1] += dest-sour

    return [[s[0], s[1]] for s in sub]

result = float("inf")
for i in range(len(seeds)//2):
    cat = "seed"
    ranges = [[seeds[2*i], seeds[2*i]+seeds[2*i+1]-1]]

    while cat != "location":
        cat = map[cat]
        new_ranges = []
        for r in ranges:
            new_ranges += convert_range(*r, cat)
        ranges = new_ranges.copy()

    m = min([r[0] for r in ranges])
    if m < result:
        result = m

print(f"part II: {result}")

