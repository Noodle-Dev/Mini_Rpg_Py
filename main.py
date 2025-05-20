import config as cfg
import pygame

pygame.init() # INIT PYGAME

screen = pygame.display.set_mode((cfg.WIDTH, cfg.LENGTH))

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)
    screen.fill("purple")
    pygame.display.flip()

pygame.quit()
