import os
import pygame
from . import sprite


class Character:
    """
    character grid size = 23x16
    character rect size = 21x14
    """

    def __init__(self):
        self.clothes = {
            'cap': None,
            'shirt': None,
            }
        self.spritesheet = sprite.Sprite('core/sprites/character.png')
        self.inventory = []
        # here is money
        self.wallet = 0

    def get_sprite(self):
        rect = (0, 0, 16, 23)
        return self.spritesheet.return_animation("idle")


