import pygame


class Sprite:
    """
    http://www.pygame.org/wiki/Spritesheet
    """

    def __init__(self, filename):
        self.sprite_index = 0
        self.sheet = pygame.image.load(filename)
        self.ANIMATION_SPEED = 10

    def image_at(self, rect):
        # Loads image from x,y,x+offset,y+offset
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size)
        self.image.blit(self.sheet, (0, 0), rect)
        return self.image

    def return_animation(self, action, time):
        if action == "idle": 
            self.rects = [
                pygame.Rect(0, 0, 16, 23),
                pygame.Rect(16, 0, 16, 23),
                pygame.Rect(32, 0, 16, 23),
            ]
        if action == "move_right":
            self.rects = [
                pygame.Rect(0, 23, 16, 23),
                pygame.Rect(16, 23, 16, 23),
                pygame.Rect(32, 23, 16, 23),
            ]
        if action == "move_left":
            self.rects = [
                pygame.Rect(0, 46, 16, 23),
                pygame.Rect(16, 46, 16, 23),
                pygame.Rect(32, 46, 16, 23),
            ]
        if action == "move_up":
            self.rects = [
                pygame.Rect(0, 69, 16, 23),
                pygame.Rect(16, 69, 16, 23),
                pygame.Rect(32, 69, 16, 23),
            ]
        if action == "move_down":
            self.rects = [
                pygame.Rect(0, 92, 16, 23),
                pygame.Rect(16, 92, 16, 23),
                pygame.Rect(32, 92, 16, 23),
            ]
        self.animation = [
            self.image_at(rect) for rect in self.rects 
        ]
        if time % self.ANIMATION_SPEED == 0:
            if self.sprite_index >= 2:
                self.sprite_index = 0
            else:
                self.sprite_index += 1
        return self.animation[self.sprite_index]