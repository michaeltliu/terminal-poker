import random

class Table:
    def __init__(self):
        self.players = []
        self.players.append(Human(self))
        for i in range(8):
            self.players.append(CPU(self))
            
        self.deck = list(range(52))
        self.community = []
        self.turn = 0
        self.button = 0
        self.callAmt = 0
        self.potSize = 0
        self.street = 0

    def newHand(self):
        self.deck = list(range(52))
        self.community = []
        self.turn = 0
        self.button += 1
        self.button %= len(self.players)
        self.callAmt = 0
        self.potSize = 0
        self.street = 0
        
    def next(self):
        self.turn += 1
        self.turn %= len(self.players)

    def dealPlayers(self):
        for player in self.players:
            hole = random.sample(self.deck, 2)
            player.hand.extend(hole)
            for i in hole:
                self.deck.remove(i)

    def dealFlop(self):
        #flop = random.sample(self.deck, 3)
        flop = [0,13,11]
        self.community.extend(flop)
        for i in flop:
            self.deck.remove(i)
        self.street = 1

    def dealTurn(self):
        #turn = random.sample(self.deck, 1)
        turn = [24]
        self.community.extend(turn)
        for i in turn:
            self.deck.remove(i)
        self.street = 2

    def dealRiver(self):
        river = random.sample(self.deck, 1)
        self.community.extend(river)
        for i in river:
            self.deck.remove(i)
        self.street = 3
                
class Player:
    def __init__(self, table):
        self.table = table
        self.hand = []
        self.stack = 1000
        self.chipsInThisRound = 0
        
    def raiseTo(self, amt):
        if amt > callAmt:
            self.stack -= amt
            table.potSize += amt
            table.callAmt = amt
        else:
            print("Raise must be higher than current call amount.")

    def call(self):
        x = table.callAmt - self.chipsInThisRound
        self.stack -= x
        table.potSize += x
        chipsInThisRound += x

    def fold(self):
        pass

class CPU(Player):
    def __init__(self, table):
        super().__init__(table)

    def move(self):
        call()

class Human(Player):
    def __init__(self, table):
        super().__init__(table)

    def move(self):
        move = input("Raise to: r <amt>, Call: c, Fold: f")
        if move[0] == "r":
            raiseTo(move[2:])
        elif move[0] == "c":
            call()
        elif move[0] == "f":
            fold()
        
class Toolkit():
    def __init__(self, table, player):
        self.table = table
        self.player = player
        self.hand = player.hand

        self.rankFreq = {}
        for i in self.hand:
            self.rankFreq[i % 13] = self.rankFreq.get(i % 13, 0) + 1
        for i in self.table.community:
            self.rankFreq[i % 13] = self.rankFreq.get(i % 13, 0) + 1

    def highCard(self):
        return max(self.hand + self.table.community)

    def pairs(self):
        pairs = []
        for i in self.rankFreq.keys():
            if self.rankFreq.get(i, 0) == 2:
                pairs.append(i)

        return pairs

    def bestTwoPair(self):
        pairs = self.pairs()

        if len(pairs) == 0: return None

        l = []
        x = max(pairs)
        l.append(x)
        pairs.remove(x)

        if len(pairs) == 0: return None
        
        l.append(max(pairs))
        return l

    def trips(self):
        trips = []
        for i in self.rankFreq.keys():
            if self.rankFreq.get(i, 0) == 3:
                trips.append(i)

        return trips

    def straight(self):
        a, b = 13, 12
        while a - b < 5:
            if self.rankFreq.get(a % 13, 0) == 0:
                a = b
                b = a - 1
            elif self.rankFreq.get(b, 0) > 0:
                b -= 1
            elif self.rankFreq.get(b, 0) == 0:
                a = b - 1
                b = a - 1

            if a < 0:
                return None
        return [b + 1, a]

    def flush(self):
        suit = {}
        for i in self.hand:
            suit[int(i/13)] = suit.get(int(i/13), 0) + 1
        for i in self.table.community:
            suit[int(i/13)] = suit.get(int(i/13), 0) + 1

        for s in suit.keys():
            if suit.get(s, 0) == 5:
                return s

        return None

    def house(self):
        pairs = self.pairs()
        trips = self.trips()
        quads = self.quads()

        if (len(trips) >= 1 or len(quads) >= 1) and len(pairs) + len(trips) + len(quads) >= 2:
            top = trips + quads
            topmax = max(top)
            top.remove(topmax)

            bottom = pairs + top
            bottommax = max(bottom)
            
            l = [topmax, bottommax]
            return l
                
        else: return None

    def quads(self):
        quads = []
        for i in self.rankFreq.keys():
            if self.rankFreq.get(i, 0) == 4:
                quads.append(i)

        return quads


table = Table()
table.dealFlop()
table.dealTurn()
table.dealPlayers()
table.dealRiver()
print(table.community)
for player in table.players:
    print(player.hand)
    kit = Toolkit(table, player)
    print(kit.highCard(), kit.pairs(), kit.bestTwoPair(), kit.trips(), kit.straight(), kit.flush(), kit.house(), kit.quads())
