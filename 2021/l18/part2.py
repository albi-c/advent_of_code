from ..advent import Advent, math

DIGITS = "0123456789"

advent = Advent(18, 2)

class Node:
    def __init__(self):
        self.parent = None
    
    def __repr__(self) -> str:
        return "<Node>"
    
    def nest_level(self):
        if self.parent is None:
            return 0
        
        return self.parent.nest_level() + 1
    
    def explode(self):
        return False
    
    def split(self):
        return False
    
    def reduce(self):
        while True:
            if self.explode():
                continue
            if self.split():
                continue

            break
        
        return self
    
    def copy(self):
        return Node()

class Number(Node):
    def __init__(self, value):
        super().__init__()

        self.value = int(value)
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def split(self):
        if self.value >= 10:
            self.parent.replace_self(self, Pair(Number(math.floor(self.value / 2)), Number(math.ceil(self.value / 2))))
            return True
        
        return False
    
    def add_lm(self, n):
        self.value += n.value
    
    def add_rm(self, n):
        self.value += n.value
    
    def magnitude(self):
        return self.value
    
    def copy(self):
        return Number(self.value)

class Pair(Node):
    def __init__(self, left, right):
        super().__init__()

        self.left = left
        self.left.parent = self

        self.right = right
        self.right.parent = self
    
    def __repr__(self) -> str:
        return f"[{self.left}, {self.right}]"
    
    def explode(self):
        if self.left.explode():
            return True
        if self.right.explode():
            return True
        
        if self.nest_level() >= 4:
            w = self.parent.which(self)

            if w == 0:
                self.add_left(w, self.left)
                self.parent.right.add_lm(self.right)
            elif w == 1:
                self.add_right(w, self.right)
                self.parent.left.add_rm(self.left)

            self.parent.replace_self(self, Number(0))

            return True
        
        return False
    
    def add_left(self, p, n):
        if self.parent is not None:
            if p == 0:
                self.parent.add_left(self.parent.which(self), n)
            else:
                self.left.add_rm(n)
        else:
            if p == 1:
                self.left.add_rm(n)
    
    def add_rm(self, n):
        self.right.add_rm(n)
    
    def add_right(self, p, n):
        if self.parent is not None:
            if p == 1:
                self.parent.add_right(self.parent.which(self), n)
            else:
                self.right.add_lm(n)
        else:
            if p == 0:
                self.right.add_lm(n)
    
    def add_lm(self, n):
        self.left.add_lm(n)
    
    def split(self):
        if self.left.split():
            return True
        if self.right.split():
            return True
        
        return False
    
    def which(self, o):
        if o == self.left:
            return 0
        elif o == self.right:
            return 1
        
        return -1
    
    def replace_self(self, o, n):
        if o == self.left:
            self.left = n
            self.left.parent = self
        elif o == self.right:
            self.right = n
            self.right.parent = self
    
    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()
    
    def copy(self):
        lc = self.left.copy()
        rc = self.right.copy()
        p = Pair(lc, rc)
        self.left.parent = p
        self.right.parent = p

        return p

def parse_pair(txt: str, i: int = 0):
    i += 1

    if txt[i] in DIGITS:
        left = Number(txt[i])
        i += 1
    else:
        left, i = parse_pair(txt, i)
    
    i += 1

    if txt[i] in DIGITS:
        right = Number(txt[i])
        i += 1
    else:
        right, i = parse_pair(txt, i)

    i += 1
    
    return Pair(left, right), i

pairs = advent.read.lines(lambda x: parse_pair(x)[0])

largest = 0

for pair in pairs:
    for p in pairs:
        if pair == p:
            continue

        m = Pair(pair.copy(), p.copy()).reduce().magnitude()
        if m > largest:
            largest = m

advent.solution(largest)
