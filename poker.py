import random

class Table:
    def __init__(self):
        self.players = []
        self.players.append(Human(self))
        for i in range(20):
            self.players.append(CPU(self))
        self.deck = list(range(1,53))
        self.community = []
        self.turn = 0
        self.button = 0
        self.callAmt = 0
        self.potSize = 0
        
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
        flop = random.sample(self.deck, 3)
        self.community.extend(flop)
        for i in flop:
            self.deck.remove(i)

    def dealTurn(self):
        turn = random.sample(self.deck, 1)
        self.community.extend(turn)
        for i in turn:
            self.deck.remove(i)

    def dealRiver(self):
        river = random.sample(self.deck, 1)
        self.community.extend(river)
        for i in river:
            self.deck.remove(i)
        
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
    def __init__(self, table):
        self.table = table
    def pair():
        pass

table = Table()
table.dealPlayers()
for player in table.players:
    print(player.hand)
table.dealFlop()
print(table.community)
