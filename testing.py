import pygame
from animation.py import walk_animation
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
 
player = walk_animation()
x, y = 300, 200
 
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    keys = pygame.key.get_pressed()
    direction = player.direction
    walking = True
 
    if keys[pygame.K_LEFT]:
        x -= 3
        direction = "left"
    elif keys[pygame.K_RIGHT]:
        x += 3
        direction = "right"
    elif keys[pygame.K_UP]:
        y -= 3
        direction = "up"
    elif keys[pygame.K_DOWN]:
        y += 3
        direction = "down"
    else:
        walking = False
 
    player.update(direction, walking)
 
    screen.fill((40, 44, 52))
    screen.blit(player.get_image(), (x, y))
    pygame.display.flip()
 
