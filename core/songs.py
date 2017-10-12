from .song import Song


class MiamiDreams(Song):

    def __init__(self):
        self.artist = "Turboway ターボ道"
        self.song_name = "Miami Dreams"
        self.file_path = 'core/music/miami_dreams.mp3'
        self.cover = None
        super().__init__(self.cover, self.artist, self.song_name, self.file_path)