# Advent of Code 2023 - Day 1

# ================ part I ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]
result = 0
for l in t:
    i, j, k = 0,len(l)-1,''
    g,d=1,1
    while i<len(l) and j>=0 and (g or d):
        if l[i].isdigit() and g:
            k = l[i]+k
            g=0
        if l[j].isdigit() and d:
            k = k+l[j]
            d=0
        i+=1
        j-=1
    result += int(k)

print(f"part I: {result}")

# ================ part II ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

dic = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
result = 0
for l in t:
    id_min,nb_min = len(l),None
    id_max,nb_max = 0,None
    for k in dic:
        i = l.find(k)
        if i != -1 and i < id_min:
            id_min = i
            nb_min = k
        i = l.rfind(k)
        if i != -1 and i > id_max:
            id_max = i
            nb_max = k

    l1, l2 = l, l
    if nb_min is not None: l1 = l1.replace(nb_min, dic[nb_min])
    if nb_max is not None: l2 = l2.replace(nb_max, dic[nb_max])

    k = ""
    i, find = len(l2)-1, False
    while not find:
        if l2[i].isdigit():
            k = l2[i]+k
            find = True
        i -= 1
    i, find = 0, False
    while not find:
        if l1[i].isdigit():
            k = l1[i]+k
            find = True
        i += 1

    result += int(k)

print(f"part II: {result}")
