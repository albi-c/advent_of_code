from ..advent import Advent

DIGITS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

advent = Advent(8, 2)

displays = list(map(lambda x: list(map(lambda y: y.split(), x.split(" | "))), advent.read.lines()))

def dig_to_num(dig):
    return DIGITS["".join(sorted(dig))]

def usages(display, seg):
    u = 0

    for d in display:
        if seg in d:
                u += 1
    
    return u

def decode_display(display):
    disp = [set(disp) for disp in display]
    m = {}
    s = {}

    for d in disp:
        if len(d) == 2:
            m[1] = d
        elif len(d) == 3:
            m[7] = d
        elif len(d) == 4:
            m[4] = d
        elif len(d) == 7:
            m[8] = d
    
    # A
    
    s["a"] = list(m[1] ^ m[7])[0]

    # B, E

    l5 = [d for d in disp if len(d) == 5]

    for d in l5:
        for seg in d:
            if usages(l5, seg) == 1:
                if seg in m[4]:
                    s["b"] = seg
                else:
                    s["e"] = seg

    # C, F
    
    for d in l5:
        if not any([usages(l5, seg) == 1 for seg in d]):
            m[3] = d
            continue
        
        for seg in d:
            if usages(l5, seg) == 2:
                if s["b"] in d:
                    m[5] = d
                    s["f"] = seg
                elif s["e"] in d:
                    m[2] = d
                    s["c"] = seg
    
    # D

    l6 = [d for d in disp if len(d) == 6]

    for d in l6:
        for seg in d:
            if usages(l6, seg) == 2:
                if seg != s["c"] and seg != s["e"]:
                    s["d"] = seg
    
    # G

    s["g"] = list(set(s.values()) ^ m[8])[0]

    return {"".join(sorted("".join(v))): k for k, v in s.items()}

result = 0

for display in displays:
    s = decode_display(display[0])

    n = 0

    for i, digit in enumerate(display[1]):
        digit = "".join([s[c] for c in digit])

        n += 10 ** (3 - i) * dig_to_num(digit)
    
    result += n

advent.solution(result)
