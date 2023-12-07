# Advent of Code 2023 - Day 4

# ================ part I ================
"""
"""

t=open('i.txt').readlines()

result = 0
for l in t:
    l = l.strip().split(': ')[1].split(' | ')
    dic = {int(i):None for i in l[0].split()}

    score = 0
    for i in l[1].split():
        if int(i) in dic:
            if score == 0: score = 1
            else: score *= 2

    result += score



print(f"part I: {result}")

# ================ part II ================
"""
"""

t=open('i.txt').readlines()

cards = []
for l in t:
    l = l.strip().split(': ')[1].split(' | ')
    dic = {int(i):None for i in l[0].split()}

    match = 0
    for i in l[1].split():
        match += int(i) in dic

    cards.append(match)

result = 0
temp = [1 for _ in range(len(cards))]
for i in range(len(temp)):
    for j in range(cards[i]):
        temp[i+j+1] += temp[i]
    result += temp[i]

print(f"part II: {result}")

