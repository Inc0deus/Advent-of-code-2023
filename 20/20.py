# Advent of Code 2023 - Day 20

# ================ part I ================
"""
"""

def partI():
    file = open("i.txt")
    l = file.readline()
    modules = {}
    TYPE, DEST, DATA = 0,1,2
    while l:
        mod, dest = l.strip().split(" -> ")
        dest = dest.split(", ")
        if mod[0] == "%":   # Flip-flop
            modules[mod[1:]] = ["%", dest, False]
        elif mod[0] == "&": # Conjunction
            modules[mod[1:]] = ["&", dest, {}]
        else:               # Broadcast
            modules[mod] = ["b", dest, None]
        l = file.readline()

    # parse conjonction inputs
    for mod in modules:
        for dest in modules[mod][DEST]:
            if dest not in modules: continue
            if modules[dest][TYPE] == "&":
                modules[dest][DATA][mod] = False

    def pushButton():
        nb_low, nb_high = 0, 0
        pulses = [("broadcaster", False, "button")]
        while pulses != []:
            mod, pulse, parent = pulses.pop(0)
            if pulse: nb_high += 1
            else: nb_low += 1

            if mod not in modules: continue

            if modules[mod][TYPE] == "b":
                for dest in modules[mod][DEST]:
                    pulses.append((dest, pulse, mod))
            elif modules[mod][TYPE] == "%":
                if pulse == True: continue
                else:
                    modules[mod][DATA] = not modules[mod][DATA]
                    for dest in modules[mod][DEST]:
                        pulses.append((dest, modules[mod][DATA], mod))
            elif modules[mod][TYPE] == '&':
                modules[mod][DATA][parent] = pulse
                conj = True
                for p in modules[mod][DATA]:
                    conj &= modules[mod][DATA][p]
                for dest in modules[mod][DEST]:
                    pulses.append((dest, not conj, mod))

        return nb_low, nb_high

    nb_low, nb_high = 0, 0
    for _ in range(1000):
        l, h = pushButton()
        nb_low += l
        nb_high += h
    
    return nb_low * nb_high

print(f"part I: {partI()}")

# ================ part II ================
"""
"""

def partII():
    file = open("i.txt")
    l = file.readline()
    modules = {}
    inputs = {"broadcaster": None}
    TYPE, DEST, DATA = 0,1,2
    while l:
        mod, dest = l.strip().split(" -> ")
        dest = dest.split(", ")
        if mod[0] == "%":   # Flip-flop
            mod = mod[1:]
            modules[mod] = ["%", dest, False]
        elif mod[0] == "&": # Conjunction
            mod = mod[1:]
            modules[mod] = ["&", dest, {}]
        else:               # Broadcast
            modules[mod] = ["b", dest, None]

        for d in dest:
            if d in inputs: inputs[d].append(mod)
            else: inputs[d] = [mod]

        l = file.readline()

    # parse conjonction inputs
    for mod in modules:
        for dest in modules[mod][DEST]:
            if dest not in modules: continue
            if modules[dest][TYPE] == "&":
                modules[dest][DATA][mod] = False

    def gcd(a, b):
        while b:      
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)


    mod_to_find = inputs["tg"]
    cycle_of = {}
    prev = {m: 0 for m in mod_to_find}
    count = {m: 0 for m in mod_to_find}

    finished = False
    i = 1
    while not finished:
        pulses = [("broadcaster", False, "button")]
        while pulses != []:
            mod, pulse, parent = pulses.pop(0)

            if not pulse and mod in mod_to_find:
                if mod in prev and count[mod] == 2:
                    cycle_of[mod] = i - prev[mod]
                prev[mod] = i
                count[mod] += 1

            if len(cycle_of) == len(mod_to_find): finished = True; break


            if mod not in modules: continue

            if modules[mod][TYPE] == "b":
                for dest in modules[mod][DEST]:
                    pulses.append((dest, pulse, mod))
            elif modules[mod][TYPE] == "%":
                if pulse == True: continue
                else:
                    modules[mod][DATA] = not modules[mod][DATA]
                    for dest in modules[mod][DEST]:
                        pulses.append((dest, modules[mod][DATA], mod))
            elif modules[mod][TYPE] == '&':
                modules[mod][DATA][parent] = pulse
                conj = True
                for p in modules[mod][DATA]:
                    conj &= modules[mod][DATA][p]
                for dest in modules[mod][DEST]:
                    pulses.append((dest, not conj, mod))

        i += 1
    
    tot = 1
    for m in cycle_of:
        tot = lcm(tot, cycle_of[m])

    return tot

print(f"part II: {partII()}")

