import pygame
import sys
from sprites import *
from config import *

class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("Arial", 32)
        self.running = True

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player

    def update(self):
        pass
    def draw(self):
        pass
    def main(self):
        pass
    def game_over(self):
        pass
    def intro_screen(self):
        pass