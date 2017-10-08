import pygame


class Sprite:
    """
    http://www.pygame.org/wiki/Spritesheet
    """

    def __init__(self, filename):
        self.sprite_index = 0
        self.sheet = pygame.image.load(filename)

    def image_at(self, rect):
        # Loads image from x,y,x+offset,y+offset
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size)
        self.image.blit(self.sheet, (0, 0), rect)
        return self.image

    def return_animation(self, action):
        if action == "idle": 
            self.rects = [
                pygame.Rect(0, 0, 16, 23),
                pygame.Rect(16, 0, 16, 23),
                pygame.Rect(32, 0, 16, 23),
            ]
            self.animation = [
                self.image_at(rect) for rect in self.rects 
            ]
            if self.sprite_index >= 2:
                self.sprite_index = 0
            else:
                self.sprite_index += 1
        return self.animation[self.sprite_index]