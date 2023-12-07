# Advent of Code 2023 - Day 7

# ================ part I ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

types = [[] for _ in range(7)]
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# return True if h1 is the best
def compare(h1, h2):
    if h1 == []: return False
    c1, c2 = cards.index(h1[0]), cards.index(h2[0])
    return c1 < c2 or (c1 == c2 and compare(h1[1:], h2[1:]))

def fusion(l1, l2):
    l = []
    i,j = 0,0
    while i < len(l1) and j < len(l2):
        if compare(l1[i][0], l2[j][0]):
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    if j == len(l2):
        l += l1[i:]
    else:
        l += l2[j:]

    return l

def sort_fus(l):
    n = len(l)
    if n <= 1: return l
    l1, l2 = sort_fus(l[:n//2]), sort_fus(l[n//2:])
    return fusion(l1, l2)
    
for l in t:
    l = l.split()
    h = l[0]
    nb_cards = []
    for c in cards:
        n = h.count(c)
        if n != 0: nb_cards.append(n)
    nb_cards.sort(reverse=True)

    if nb_cards[0] == 5:                        # Five of a kind
        types[0].append((h, int(l[1])))
    elif nb_cards[0] == 4:                      # Four of a kind
        types[1].append((h, int(l[1])))
    elif nb_cards[0] == 3 and nb_cards[1] == 2: # Full house
        types[2].append((h, int(l[1])))
    elif nb_cards[0] == 3:                      # Three of a kind
        types[3].append((h, int(l[1])))
    elif nb_cards[0] == 2 and nb_cards[1] == 2: # Two pair
        types[4].append((h, int(l[1])))
    elif nb_cards[0] == 2:                      # One pair
        types[5].append((h, int(l[1])))
    else:                                       # High card
        types[6].append((h, int(l[1])))

result = 0
k = 0
for i in range(len(types)):
    for h in sort_fus(types[i]):
        result += h[1] * (len(t)-k)
        k += 1

print(f"part I: {result}")

# ================ part II ================
"""
"""

t=[l.strip() for l in open('i.txt').readlines()]

types = [[] for _ in range(7)]
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

# return True if h1 is the best
def compare(h1, h2):
    if h1 == []: return False
    c1, c2 = cards.index(h1[0]), cards.index(h2[0])
    return c1 < c2 or (c1 == c2 and compare(h1[1:], h2[1:]))

def fusion(l1, l2):
    l = []
    i,j = 0,0
    while i < len(l1) and j < len(l2):
        if compare(l1[i][0], l2[j][0]):
            l.append(l1[i])
            i += 1
        else:
            l.append(l2[j])
            j += 1
    if j == len(l2):
        l += l1[i:]
    else:
        l += l2[j:]

    return l

def sort_fus(l):
    n = len(l)
    if n <= 1: return l
    l1, l2 = sort_fus(l[:n//2]), sort_fus(l[n//2:])
    return fusion(l1, l2)

def hand_possible(wanted, hand, nb_jokers):
    J = nb_jokers
    possible = True
    for i in range(len(wanted)):
        if i >= len(hand):
            if J-wanted[i] >= 0:
                J -= wanted[i]
                continue
            else:
                possible = False
                break
        elif hand[i] == wanted[i]: continue
        elif hand[i]+J >= wanted[i]:
            J -= wanted[i]-hand[i]
        else:
            possible = False
            break

    return possible

for l in t:
    l = l.split()
    h = l[0]
    nb_cards = []
    J = 0
    for c in cards:
        if c == "J": J = h.count(c)
        else:
            n = h.count(c)
            if n != 0: nb_cards.append(n)
    nb_cards.sort(reverse=True)

    if hand_possible([5],nb_cards,J):       # Five of a kind
        types[0].append((h, int(l[1])))
    elif hand_possible([4],nb_cards,J):     # Four of a kind
        types[1].append((h, int(l[1])))
    elif hand_possible([3,2],nb_cards,J):   # Full house
        types[2].append((h, int(l[1])))
    elif hand_possible([3],nb_cards,J):     # Three of a kind
        types[3].append((h, int(l[1])))
    elif hand_possible([2,2],nb_cards,J):   # Two pair
        types[4].append((h, int(l[1])))
    elif hand_possible([2],nb_cards,J):     # One pair
        types[5].append((h, int(l[1])))
    else:                                   # High card
        types[6].append((h, int(l[1])))

result = 0
k = 0
for i in range(len(types)):
    for h in sort_fus(types[i]):
        result += h[1] * (len(t)-k)
        k += 1

print(f"part II: {result}")

