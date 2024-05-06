# Advent of Code 2023 - Day 19

# ================ part I ================
"""
"""

def partI():
    f = open("i.txt")
    l = f.readline()
    workflows = {"A":None, "R":None}
    GS,LS = 0,1 # greater, less (strict)
    while l != "\n":
        wf, cond = l.strip()[:-1].split("{")
        cond = cond.split(",")
        for i in range(len(cond)-1):
            c, nwf = cond[i].split(":")
            categ = c[0]
            comp = GS if c[1]==">" else LS
            n = int(c[2:])
            cond[i] = (categ, comp, n, nwf)
        workflows[wf] = cond
        l = f.readline()

    parts = []
    l = f.readline()
    while l:
        p = l.strip()[1:-1].split(",")
        rating = {}
        for i in range(4):
            rating[p[i][0]]= int(p[i][2:])
        parts.append(rating)
        l = f.readline()

    def passRule(part, rule):
        categ, comp, n, _ = rule
        if comp == GS:
            return part[categ] > n
        else:
            return part[categ] < n

    def isAccepted(part, wf):
        if wf == "A": return True
        if wf == "R": return False

        for rule in workflows[wf][:-1]:
            if passRule(part, rule):
                return isAccepted(part, rule[-1])
        return isAccepted(part, workflows[wf][-1])
    
    tot = 0
    for i in range(len(parts)):
        if isAccepted(parts[i], "in"):
            tot += parts[i]["x"] + parts[i]["m"] + parts[i]["a"] + parts[i]["s"]

    return tot

print(f"part I: {partI()}")

# ================ part II ================
"""
"""

def partII():
    t=[l.strip() for l in open('i.txt').readlines()]

    f = open("i.txt")
    l = f.readline()
    workflows = {"A":None, "R":None}
    GS,LS = 0,1 # greater, less
    while l != "\n":
        wf, cond = l.strip()[:-1].split("{")
        cond = cond.split(",")
        for i in range(len(cond)-1):
            c, nwf = cond[i].split(":")
            categ = c[0]
            comp = GS if c[1]==">" else LS
            n = int(c[2:])
            cond[i] = (categ, comp, n, nwf)
        workflows[wf] = cond
        l = f.readline()


    def nextWorkflow(parts, wf):
        if wf == "A":
            nx = parts["x"][1] - parts["x"][0] + 1
            nm = parts["m"][1] - parts["m"][0] + 1
            na = parts["a"][1] - parts["a"][0] + 1
            ns = parts["s"][1] - parts["s"][0] + 1
            return nx*nm*na*ns
        if wf == "R": return 0

        tot = 0

        for rule in workflows[wf][:-1]:
            categ, comp, n, nwf = rule
            categ_range = parts[categ]
            if comp == GS:  # n ?< [[0]..[1]]
                if categ_range[0] > n:
                    tot += nextWorkflow(parts, nwf)
                elif categ_range[1] < n:
                    continue
                else:
                    temp_parts = parts.copy()
                    temp_parts[categ] = (n+1, parts[categ][1])
                    tot += nextWorkflow(temp_parts, nwf)

                    parts[categ] = (parts[categ][0], n)
                    continue
            
            elif comp == LS:  # [[0]..[1]] ?< n
                if categ_range[1] < n:
                    tot += nextWorkflow(parts, nwf)
                elif categ_range[0] > n:
                    continue
                else:
                    temp_parts = parts.copy()
                    temp_parts[categ] = (temp_parts[categ][0], n-1)
                    tot += nextWorkflow(temp_parts, nwf)

                    parts[categ] = (n, parts[categ][1])
                    continue

        tot += nextWorkflow(parts, workflows[wf][-1])

        return tot

    parts = {"x":(1,4000), "m":(1,4000), "a":(1,4000), "s":(1,4000)}
    return nextWorkflow(parts, "in")

print(f"part II: {partII()}")

