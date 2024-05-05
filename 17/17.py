# Advent of Code 2023 - Day --

# ================ part I ================
"""
"""

from heapq import heappush, heappop

def partI():
    t=[list(map(int, l.strip())) for l in open('i.txt').readlines()]
    R,C = len(t), len(t[0])

    dist = {(0, 0, 0, 0, 0):0}
    queue = [[0, 0, 0, 0, 0, 0]]
    seen = []

    final_cost = 0
    total_possibilities = R*C*4*3

    # Dijkstra
    while queue != []:
        print(len(queue), round(100*len(seen)/total_possibilities, 3))
        cost, r, c, dr, dc, count = heappop(queue)

        if r == R-1 and c == C-1:
            final_cost = cost
            break

        seen.append((r,c,dr,dc,count))
        
        # try moving forward
        if count < 3 and (dr,dc) != (0,0):
            nr = r+dr
            nc = c+dc
            if 0<= nr < R and 0 <= nc < C:
                if (nr,nc,dr,dc,count+1) not in dist or ((nr,nc,dr,dc,count+1) in dist and dist[(nr,nc,dr,dc,count+1)] > cost + t[nr][nc]) and (nr,nc,dr,dc,count+1) not in seen:
                    heappush(queue, (cost + t[nr][nc], nr, nc, dr, dc, count+1))
                    dist[(nr,nc,dr,dc,count+1)] = cost + t[nr][nc]

        # try turning
        for ndr,ndc in [(1,0),(-1,0),(0,1),(0,-1)]:
            if (ndr,ndc) != (dr,dc) and (ndr,ndc) != (-dr,-dc):
                nr = r+ndr
                nc = c+ndc
                if 0<= nr < R and 0 <= nc < C:
                    if (nr,nc,ndr,ndc,1) not in dist or ((nr,nc,ndr,ndc,1) in dist and dist[(nr,nc,ndr,ndc,1)] > cost + t[nr][nc]) and (nr,nc,ndr,ndc,1) not in seen:
                        heappush(queue, (cost + t[nr][nc], nr, nc, ndr, ndc, 1))
                        dist[(nr,nc,ndr,ndc,1)] = cost + t[nr][nc]

    return final_cost

# print(f"part I: {partI()}")

# ================ part II ================
"""
"""

from heapq import heappush, heappop

def partII():
    t=[list(map(int, l.strip())) for l in open('i.txt').readlines()]
    R,C = len(t), len(t[0])

    dist = {(0, 0, 0, 0, 0):0}
    queue = [[0, 0, 0, 0, 0, 0]]
    seen = []

    final_cost = 0
    total_possibilities = R*C*4*10

    # Dijkstra
    while queue != []:
        print(len(queue), round(100*len(seen)/total_possibilities, 3))
        cost, r, c, dr, dc, count = heappop(queue)

        if r == R-1 and c == C-1 and count >= 4:
            final_cost = cost
            break

        seen.append((r,c,dr,dc,count))

        if count < 10 and (r,c) != (0,0): # try moving forward
            nr = r+dr
            nc = c+dc
            if 0<= nr < R and 0 <= nc < C:
                if (nr,nc,dr,dc,count+1) not in dist or ((nr,nc,dr,dc,count+1) in dist and dist[(nr,nc,dr,dc,count+1)] > cost + t[nr][nc]) and (nr,nc,dr,dc,count+1) not in seen:
                    heappush(queue, (cost + t[nr][nc], nr, nc, dr, dc, count+1))
                    dist[(nr,nc,dr,dc,count+1)] = cost + t[nr][nc]

        if count >= 4 or (r,c) == (0,0): # try turning
            for ndr,ndc in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (ndr,ndc) != (dr,dc) and (ndr,ndc) != (-dr,-dc):
                    nr = r+ndr
                    nc = c+ndc
                    if 0<= nr < R and 0 <= nc < C:
                        if (nr,nc,ndr,ndc,1) not in dist or ((nr,nc,ndr,ndc,1) in dist and dist[(nr,nc,ndr,ndc,1)] > cost + t[nr][nc]) and (nr,nc,ndr,ndc,1) not in seen:
                            heappush(queue, (cost + t[nr][nc], nr, nc, ndr, ndc, 1))
                            dist[(nr,nc,ndr,ndc,1)] = cost + t[nr][nc]

    return final_cost

print(f"part I: {partII()}")

