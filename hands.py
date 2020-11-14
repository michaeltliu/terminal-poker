class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
class Table:
    def __init__(self):
        self.public = []

def compareHands(h1, h2):
    pass

# Highest rank is [0], second highest is [1], etc.
def highCard(cards):
    l = []
    for c in cards:
        l.append(c.rank)
    l.sort(reverse = True)
    return l[:5]

# Two pair if len() >= 2, no pair if len == 0
def pair(cards):
    d = dict()
    for c in cards:
        r = c.rank
        d[r] = d.get(r, 0) + 1
    ret = []
    for k in d.keys():
        if d.get(k, 0) == 2:
            ret.append(k)
    ret.sort(reverse = True)
    return ret

def trips(cards):
    d = dict()
    for c in cards:
        r = c.rank
        d[r] = d.get(r, 0) + 1
    ret = []
    for k in d.keys():
        if d.get(k, 0) == 3:
            ret.append(k)
    ret.sort(reverse = True)
    return ret

def straight(cards):
    d = dict()
    for c in cards:
        r = c.rank
        d[r] = d.get(r, 0) + 1

    a, b = 14, 13
    while a - b < 5:
        if d.get(a, 0) == 0:
            a = b
            b = a - 1
        elif d.get(b, 0) > 0 or (b == 1 and d.get(14, 0) > 0):
            b -= 1
        elif d.get(b, 0) == 0 or (b == 1 and d.get(14, 0) == 0):
            a = b - 1
            b = a - 1

        if a < 1:
            return 0
    
    return a

def flush(cards):
    d = dict()
    for c in cards:
        s = c.suit
        d[s] = d.get(s, 0) + 1
    for s in d.keys():
        if d.get(s, 0) == 5:
            return s
    return 0

print(flush(
    [Card(1,1), Card(1,13), Card(2, 10), Card(2, 12), Card(2, 13), Card(2, 11), Card(2, 9)]
    ))