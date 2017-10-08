import pygame


class Location:

    def __init__(self):
        self.back = pygame.image.load('core/sprites/test_back.png')

    def draw(self, screen):
        screen.blit(self.back, dest=(0, 0))
