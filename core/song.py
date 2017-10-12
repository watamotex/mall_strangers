import pygame
from .inventory_object import InventoryObject


class Song(InventoryObject):

    def __init__(self, sprite_path, artist, song_name, file_path):
        self.artist = artist
        self.song_name = song_name
        self.file_path = file_path
        #self.sprite = pygame.image.load("sprite_path")

    def return_info(self):
        return {
            'artist': self.artist,
            'song_name': self.song_name,
            'path': self.file_path
            }