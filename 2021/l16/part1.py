from ..advent import Advent, BitList

advent = Advent(16, 1)

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

def version_sum(packet: dict) -> int:
    v = packet["version"]

    for p in packet.get("packets", []):
        v += version_sum(p)

    return v

advent.solution(version_sum(read_packet(bl)))
