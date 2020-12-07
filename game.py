from hands import *
import pygame, sys, random

pygame.init()

class Table:
    def __init__(self):
        self.deck = []
        self.public = []
        self.player = []
        self.cpu = []

        self.resetDeck()

    def resetDeck(self):
        for s in range(1, 5):
            for r in range(2, 15):
                self.deck.append(Card(s, r))
        random.shuffle(self.deck)

        self.public.clear()
        self.player.clear()
        self.cpu.clear()

    def dealPlayers(self):
        for i in range(4):
            c = self.deck.pop(0)
            if i % 2 == 0:
                self.player.append(c)
            else:
                self.cpu.append(c)

    def dealPublic(self, num):
        for i in range(num):
            c = self.deck.pop(0)
            self.public.append(c)

def drawText(screen, text, color, size, center, font = 'Comic Sans MS'):
    font = pygame.font.SysFont(font, size)
    textSurf = font.render(text, True, COLORS[color])
    textRect = textSurf.get_rect()
    textRect.center = center
    screen.blit(textSurf, textRect)

HEIGHT, WIDTH = 720, 1080        # must be multiples of 180
DIM = (WIDTH, HEIGHT)
COLORS = pygame.color.THECOLORS
table = Table()
dealButtonOn = True
button = True                   # True when human player is button

screen = pygame.display.set_mode(DIM)
pygame.display.set_caption("Bokerrrr")
screen.fill(COLORS['white'])

background = pygame.Surface(DIM)
pygame.draw.rect(background, COLORS['gray'], pygame.Rect(.25 * WIDTH, .3 * HEIGHT, .5 * WIDTH, .4 * HEIGHT))
pygame.draw.circle(background, COLORS['gray'], (.25 * WIDTH, .5 * HEIGHT), .2 * HEIGHT)
pygame.draw.circle(background, COLORS['gray'], (.75 * WIDTH, .5 * HEIGHT), .2 * HEIGHT)

dealNextRect = pygame.Rect(.4 * WIDTH, .45 * HEIGHT, .2 * WIDTH, .1 * HEIGHT)
dealNextSurf = pygame.Surface(DIM)
pygame.draw.rect(dealNextSurf, COLORS['green'], dealNextRect, 5)
drawText(dealNextSurf, "DEAL NEXT HAND", 'green', 18, (.5 * WIDTH, .5 * HEIGHT))

screen.blit(background, (0,0))
screen.blit(dealNextSurf, (0,0))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            if dealButtonOn and dealNextRect.collidepoint(pygame.mouse.get_pos()):
                table.dealPlayers()
                dealButtonOn = False