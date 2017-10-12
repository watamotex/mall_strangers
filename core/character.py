import os
import pygame
from . import sprite
from . import songs


class Character:
    """
    character grid size = 23x16
    character rect size = 21x14
    """

    def __init__(self):
        self.pos = {'x': 0, 'y': 0}
        self.SPEED = 2
        self.clothes = {
            'cap': None,
            'shirt': None,
            }
        self.spritesheet = sprite.Sprite('core/sprites/character.png')
        self.inventory = {}
        self.tapes = [songs.MiamiDreams()]
        # here is money
        self.wallet = 0
        self.current_animation = "idle"

    def get_sprite(self, time):
        rect = (0, 0, 16, 23)
        return self.spritesheet.return_animation(self.current_animation, time)

    def draw(self, screen, time):
        screen.blit(self.get_sprite(time), dest=(self.pos['x'], self.pos['y']))

    def move(self, destination):
        if destination == 'down':
            self.current_animation = "move_down"
            self.pos['y'] += self.SPEED
        elif destination == 'up':
            self.current_animation = "move_up"
            self.pos['y'] -= self.SPEED
        elif destination == 'left':
            self.current_animation = "move_left"
            self.pos['x'] -= self.SPEED
        elif destination == 'right':
            self.current_animation = "move_right"
            self.pos['x'] += self.SPEED
        else:
            self.current_animation = "idle"

    def idle(self):
        self.current_animation = "idle"

    def get_tapes(self):
        return self.tapes


