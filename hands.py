class Card:
    # Suit in [1,4]; rank in [2, 14]
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
# l1 and l2 are assumed to be monotone decreasing
def compareList(l1, l2, c = 10):
    for i in range(min(c, len(l1))):
        if l1[i] != l2[i]:
            return l1[i] - l2[i]
    return 0

# Returns a positive number if h1 is stronger than h2 and vice versa
# Returns 0 if h1 and h2 have same strength
# Does not satisfy triangle inequality
def compareHands(h1, h2):
    s1 = straightFlush(h1)[1] 
    s2 = straightFlush(h2)[1]

    if s1 != s2:
        return s1 - s2
    elif s1 > 0:
        return 0
    
    q1 = quads(h1)
    q2 = quads(h2)
    s1 = q1[0] if len(q1) > 0 else 0
    s2 = q2[0] if len(q2) > 0 else 0
    if s1 != s2:
        return s1 - s2
    elif s1 > 0:
        q1 = [card.rank for card in h1 if card.rank != s1]
        q2 = [card.rank for card in h2 if card.rank != s2]
        return max(q1) - max(q2)

    s1 = house(h1)
    s2 = house(h2)
    if s1 != s2:
        return s1[0] - s2[0] or s1[1] - s2[1]   # Returns first nonzero result
    elif s1 != (0, 0):
        return 0

    s1 = flush(h1)
    s2 = flush(h2)
    if len(s1) != len(s2):
        return len(s1) - len(s2)
    elif len(s1) > 0:
        return compareList(s1, s2)

    s1 = straight(h1)
    s2 = straight(h2)
    if s1 != s2:
        return s1 - s2
    elif s1 > 0:
        return 0

    t1 = trips(h1)
    t2 = trips(h2)
    s1 = t1[0] if len(t1) > 0 else 0
    s2 = t2[0] if len(t2) > 0 else 0
    if s1 != s2:
        return s1 - s2
    elif s1 > 0:
        t1 = [card.rank for card in h1 if card.rank != s1]
        t2 = [card.rank for card in h2 if card.rank != s2]
        t1.sort(reverse = True)
        t2.sort(reverse = True)
        return compareList(t1, t2, 2)

    p1 = pairs(h1)
    p2 = pairs(h2)
    if min(2, len(p1)) != min(2, len(p2)):      # 3 pairs is the same as 2 pairs
        return len(p1) - len(p2)
    elif len(p1) >= 2:                          # Both have at least 2 pairs
        s1_0, s1_1 = p1[0], p1[1]
        s2_0, s2_1 = p2[0], p2[1]
        if s1_0 != s2_0:
            return s1_0 - s2_0
        elif s1_1 != s2_1:
            return s1_1 - s2_1
        
        # Comes down to fifth card kicker
        p1 = [card.rank for card in h1 if (card.rank != s1_0 and card.rank != s1_1)]
        p2 = [card.rank for card in h2 if (card.rank != s2_0 and card.rank != s2_1)]
        return max(p1) - max(p2)
    elif len(p1) == 1:                          # Both only have a single pair
        s1 = p1[0]
        s2 = p2[0]
        if s1 != s2:
            return s1 - s2

        # Top 3 cards kick
        p1 = [card.rank for card in h1 if card.rank != s1]
        p2 = [card.rank for card in h2 if card.rank != s2]
        p1.sort(reverse = True)
        p2.sort(reverse = True)
        return compareList(p1, p2, 3)

    # Both players only have high card
    return compareList(highCard(h1), highCard(h2))

# Highest rank is [0], second highest is [1], etc.
def highCard(cards):
    l = []
    for c in cards:
        l.append(c.rank)
    l.sort(reverse = True)
    return l[:5]

# Two pair if len() >= 2, no pair if len == 0
def pairs(cards):
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
        if a < 5 or b < 1:
            return 0

        if d.get(a, 0) == 0:
            a = b
            b = a - 1
        elif d.get(b, 0) > 0 or (b == 1 and d.get(14, 0) > 0):
            b -= 1
        elif d.get(b, 0) == 0 or (b == 1 and d.get(14, 0) == 0):
            a = b - 1
            b = a - 1
    
    return a

def flush(cards):
    d = dict()
    for c in cards:
        s = c.suit
        temp = d.get(s, list())
        temp.append(c.rank)
        d[s] = temp
    for s in d.keys():
        ret = d.get(s, list())
        if len(ret) >= 5:
            ret.sort(reverse = True)
            return ret[:5]
    return []

def house(cards):
    pairl = pairs(cards)
    tripl = trips(cards)
    quadl = quads(cards)

    l = tripl + quadl
    if len(l) > 0:
        top = max(l)
        l.remove(top)
    else:
        return (0, 0)

    m = l + pairl
    if len(m) > 0:
        bot = max(m)
        return (top, bot)
    else:
        return (0, 0)
    
def quads(cards):
    d = dict()
    for c in cards:
        r = c.rank
        d[r] = d.get(r, 0) + 1
    ret = []
    for k in d.keys():
        if d.get(k, 0) == 4:
            ret.append(k)
    ret.sort(reverse = True)
    return ret

def straightFlush(cards):
    d = dict()
    for c in cards:
        r = c.rank
        temp = d.get(r, set())
        temp.add(c.suit)
        d[r] = temp

    for i in range(1, 5):
        a, b = 14, 13
        while a - b < 5:
            if a < 5 or b < 1:
                break
                
            if i not in d.get(a, set()):
                a = b
                b = a - 1
            elif i in d.get(b, set()) or (b == 1 and i in d.get(14, set())):
                b -= 1
            elif i not in d.get(b, set()) or (b == 1 and i not in d.get(14, set())):
                a = b - 1
                b = a - 1

        if b >= 0 and a >= 5:
            return (i, a)
    
    return (0, 0)