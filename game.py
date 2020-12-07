from hands import *
import pygame, sys, random

pygame.init()

class Table:
    def __init__(self):
        self.deck = []
        self.resetDeck()

        self.public = []
        self.player = []
        self.cpu = []

    def resetDeck(self):
        for s in range(1, 5):
            for r in range(2, 15):
                self.deck.append(Card(s, r))

        random.shuffle(self.deck)

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
COLORS = pygame.color.THECOLORS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bokerrrr")
screen.fill([255,255,255])
pygame.draw.rect(screen, COLORS['green'], pygame.Rect(.4 * WIDTH, .45 * HEIGHT, .2 * WIDTH, .1 * HEIGHT), 5)
drawText(screen, "START", 'green', 30, (.5 * WIDTH, .5 * HEIGHT))
pygame.display.update()



while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()