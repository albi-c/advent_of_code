from ..advent import Advent, BitList

advent = Advent(16, 2)

bl = advent.read.bitlist_hex()

def read_packet(bl: BitList) -> dict:
    packet = {}

    packet["version"] = bl.read.int(3)
    packet["type"] = bl.read.int(3)
    length = 6

    if packet["type"] == 4:
        n = 0

        while bl.read.bit():
            n |= bl.read.int(4)
            n <<= 4
            length += 5
        
        n |= bl.read.int(4)
        length += 5

        packet["value"] = n
    
    else:
        packet["packets"] = []

        lti = bl.read.bit()
        length += 1

        if lti:
            n = bl.read.int(11)
            length += 11

            t = 0
            for _ in range(n):
                p = read_packet(bl)
                packet["packets"].append(p)
                t += p["length"]
            length += t

        else:
            l = bl.read.int(15)
            length += 15

            t = 0
            while t < l:
                p = read_packet(bl)
                packet["packets"].append(p)
                t += p["length"]
            length += t
    
    packet["length"] = length

    return packet

def get_value(packet: dict) -> int:
    t = packet["type"]
    if t != 4:
        p = packet["packets"]

    if t == 0:
        return sum(map(get_value, p))
    elif t == 1:
        return advent.util.product(map(get_value, p))
    elif t == 2:
        return min(map(get_value, p))
    elif t == 3:
        return max(map(get_value, p))
    
    elif t == 4:
        return packet["value"]
    
    elif t == 5:
        return int(get_value(p[0]) > get_value(p[1]))
    elif t == 6:
        return int(get_value(p[0]) < get_value(p[1]))
    elif t == 7:
        return int(get_value(p[0]) == get_value(p[1]))

advent.solution(get_value(read_packet(bl)))
