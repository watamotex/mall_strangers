from pygame import mixer, image
import core.songs

class Walkman:

    def __init__(self, character_songs):
        self.tapes = character_songs
        self.sprite = image.load("core/sprites/walkman.png")
        self.open_status = False

    def load_songs(self):
        mixer.music.load(self.tapes[0].return_info()['path'])

    def play(self):
        mixer.music.play()

    def draw(self, screen):
        screen.blit(self.sprite, dest=(20, 20))

    def open(self):
        self.open_status = True

    def is_open(self):
        return self.open_status

    def close(self):
        self.open_status = False