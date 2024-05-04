# Advent of Code 2023 - Day 12

# ================ part I ================
"""
"""

def partI():
    t=[l.strip() for l in open('i.txt').readlines()]

    # parse the data in rows (???.###) and groups (1,1,3)
    rows, groups = [], []
    for l in t:
        r,g = l.split()
        rows.append(list(r))
        groups.append([int(n) for n in g.split(",")])

    # return the next arrangement to test
    def nextTest(test: list[bool]):
        i = len(test)-1
        next_test = test.copy()
        while i >= 0 and test[i]=="#":
            next_test[i] = "."
            i -= 1
        if i == -1: return None
        else:
            next_test[i] = "#"
            return next_test

    # brute force, we test every arrangements
    result = 0
    for i in range(len(rows)):
        print(i)
        row, group = rows[i], groups[i]
        nb_to_find = 0
        for s in row:
            if s == "?": nb_to_find += 1

        test_val = ["." for _ in range(nb_to_find)]
        nb_arrangements = 0
        while test_val is not None:
            test_row = row.copy()
            idx = 0
            count, test_group = 0, []
            for k in range(len(test_row)):
                # set values of "?" to the current arrangement to test
                if test_row[k] == "?":
                    test_row[k] = test_val[idx]
                    idx += 1
                
                # verification
                if test_row[k] == "#":
                    count += 1
                else:
                    if count != 0:
                        test_group.append(count)
                    count = 0
            if count != 0:
                test_group.append(count)
                
            if test_group == group:
                nb_arrangements += 1

            test_val = nextTest(test_val)

        result += nb_arrangements

    return result

# print(f"part I: {partI()}")

# ================ part II ================
"""
"""

def partII():
    t=[l.strip() for l in open('i.txt').readlines()]

    # parse the data in rows (???.###) and groups (1,1,3)
    rows, groups = [], []
    for l in t:
        r,g = l.split()
        rows.append(((r+"?")*5)[:-1])
        groups.append(tuple([int(n) for n in g.split(",")]*5))

    # dynamic function with memoïsation
    def nbArrangements(row, group, mem):
        if (row, group) in mem:
            return mem[(row, group)]

        if row == "":
            if group == (): return 1
            else: return 0
        if group == ():
            if "#" in row: return 0
            else: return 1

        tot = 0

        if row[0] in ".?":
            tot += nbArrangements(row[1:], group, mem)
        
        if row[0] in "#?":
            if group[0] <= len(row) and "." not in row[:group[0]] and (group[0] == len(row) or row[group[0]] != "#"):
                tot += nbArrangements(row[group[0]+1:], group[1:], mem)

        mem[(row, group)] = tot
        return tot
            

    tot = 0
    for i in range(len(rows)):
        row, group = rows[i], groups[i]
        tot += nbArrangements(row, group, {})
    
    return tot

print(f"part II: {partII()}")

