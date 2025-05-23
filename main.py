import pygame
import sys
from sprites import *
from config import *

class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font("Arial", 32)
        self.running = True
    
    def createTileMap(self):
        for i, row in enumerate(TILEMAP):
            for j, column in enumerate(row):
                if column == 'B':
                    Block(self, j, i)
                if column == 'P':
                    Player(self, j, i)
    
    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTileMap() 
        

    def events(self):
        #Game loop event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        #Game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self): # Game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    def game_over(self):
        pass
    def intro_screen(self):
        pass

g = main()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()