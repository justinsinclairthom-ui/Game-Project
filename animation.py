import pygame, os

class walk_animation:
    def __init__(self):
        self.direction = "down"
        self.frames = {}
        self.index = 0
        self.scale = 2

        prefixes = {"down":"wb", "up":"wf", "left":"wl", "right":"wr"}

        for direction, prefix in prefixes.items():
            self.frames[direction] = []
            for i in range(4):
                name = f"{prefix}{i}.png"
                if os.path.exists(os.path.join("characters", name)):
                    self.frames[direction].append(self.load_image(name))

    def load_image(self, image_name):
        image = pygame.image.load(os.path.join("characters", image_name)).convert_alpha()
        return pygame.transform.scale(image, (16 * self.scale, 16 * self.scale))

    def update(self, direction, walking):
        self.direction = direction
        if walking:
            self.index += 0.15   
        else:
            self.index = 0

    def get_image(self):
        frames = self.frames[self.direction]
        return frames[int(self.index) % len(frames)]
        
        