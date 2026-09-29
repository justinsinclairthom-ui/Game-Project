import pygame, sys
from animation import walk_animation
from os import path as pt

# constant variabel
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000

PLAYER_X = WINDOW_WIDTH/2
PLAYER_Y = WINDOW_HEIGHT/2


# start game
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Unknown")

floor_tile_image = pygame.image.load(pt.join("background", "A2_Ground.png"))


clock = pygame.time.Clock()

# stop or play the loop
running = True

# class enemies(pygame.Rect):
#     def __init__(self):
#         pygame.Rect.__init__(self, )

class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, 32, 32)

class Tile(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, 32, 32)
        self.image = image

# enemy = enemies()
player = Player()
animation = walk_animation()

def create_map():
    for n in range(20):
        for i in range (32):
            tile = Tile(i*32, n*31, floor_tile_image)
            tiles.append(tile)

tiles = []

def draw():
    window.fill("blue")

    for tile in tiles :
        window.blit(tile.image, tile)

    window.blit(animation.get_image(), player)
    # window.blit(animation.get_image(), enemy)

create_map()

while running:
    for input in pygame.event.get():
        if input.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

    direction = animation.direction  
    walking = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 3
        direction = "left"
    elif keys[pygame.K_d]:
        player.x += 3
        direction = "right"
    elif keys[pygame.K_w]:
        player.y -= 3
        direction = "up"
    elif keys[pygame.K_s]:
        player.y += 3
        direction = "down"
    else:
        walking = False

    animation.update(direction, walking)

    draw()
    clock.tick(60)
    pygame.display.flip()