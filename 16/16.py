# Advent of Code 2023 - Day 16

# ================ part I ================
"""
"""

def partI():
    t=[list(l.strip()) for l in open('i.txt').readlines()]
    # for l in t: print("".join(l))

    N = -1
    L = 0
    R = 1
    U = 2
    D = 3

    beams = [[(0,0), N]]
    prev_beams = {}
    energized = {}

    def update():
        new_beams = []
        for b in beams:
            if tuple(b) in prev_beams: continue

            prev_beams[tuple(b)] = True

            pos, direct = b
            energized[tuple(pos)] = True

            y,x = pos
            if direct == N: direct = R
            elif direct == R: x += 1
            elif direct == L: x -= 1
            elif direct == U: y -= 1
            elif direct == D: y += 1

            if 0<=y<len(t) and 0<=x<len(t[0]):
                tile = t[y][x]
                if tile == ".": pass
                elif tile == "/":
                    direct = 3-direct
                elif tile == "\\":
                    direct = (direct+2)%4
                elif tile == "-":
                    if direct in [U,D]:
                        direct = L
                        new_beams.append([(y,x), R])
                elif tile == "|":
                    if direct in [L,R]:
                        direct = U
                        new_beams.append([(y,x), D])

                new_beams.append([(y,x), direct])
        
        return new_beams

    def hashBeams():
        lst = [[] for _ in range(len(t[0])*len(t))]
        for p,d in beams:
            lst[p[0]*len(t[0]) + p[1]].append(d)
        
        ret = []
        for i in range(len(lst)):
            ret.append(tuple(sorted(lst[i])))
        return tuple(ret)


    while len(beams) > 0:
        beams = update()
    
    return len(energized)

print(f"part I: {partI()}")

# ================ part II ================
"""
"""

def partII():
    t=[list(l.strip()) for l in open('i.txt').readlines()]
    # for l in t: print("".join(l))

    NL = -1
    NR = -2
    NU = -3
    ND = -4
    L = 0
    R = 1
    U = 2
    D = 3

    def update(beams, saved, energized):
        new_beams = []
        for b in beams:
            if tuple(b) in saved: continue

            saved[tuple(b)] = True

            pos, direct = b
            energized[tuple(pos)] = True

            y,x = pos
            if direct == NL: direct = L
            elif direct == NR: direct = R
            elif direct == NU: direct = U
            elif direct == ND: direct = D
            elif direct == R: x += 1
            elif direct == L: x -= 1
            elif direct == U: y -= 1
            elif direct == D: y += 1

            if 0<=y<len(t) and 0<=x<len(t[0]):
                tile = t[y][x]
                if tile == ".": pass
                elif tile == "/":
                    direct = 3-direct
                elif tile == "\\":
                    direct = (direct+2)%4
                elif tile == "-":
                    if direct in [U,D]:
                        direct = L
                        new_beams.append([(y,x), R])
                elif tile == "|":
                    if direct in [L,R]:
                        direct = U
                        new_beams.append([(y,x), D])

                new_beams.append([(y,x), direct])
        
        return new_beams


    max_energized = 0

    for i in range(len(t)):
        saved, energized = {}, {}
        beams = [[(i,0), NR]]
        while len(beams) > 0:
            beams = update(beams, saved, energized)
        
        max_energized = max(max_energized, len(energized))

        saved, energized = {}, {}
        beams = [[(i,len(t[0])-1), NL]]
        while len(beams) > 0:
            beams = update(beams, saved, energized)

        max_energized = max(max_energized, len(energized))

    for j in range(len(t[0])):
        saved, energized = {}, {}
        beams = [[(0,j), ND]]
        while len(beams) > 0:
            beams = update(beams, saved, energized)
        
        max_energized = max(max_energized, len(energized))

        saved, energized = {}, {}
        beams = [[(len(t)-1,j), NU]]
        while len(beams) > 0:
            beams = update(beams, saved, energized)

        max_energized = max(max_energized, len(energized))
    
    return max_energized


print(f"part II: {partII()}")

