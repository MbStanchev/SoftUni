from OOP.class_obj_spotifay.project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        for album_song in self.songs:
            if album_song.name == song.name:
                return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for songa in self.songs:
            if songa.name != song_name:
                return "Song is not in the album."
            if self.published:
                return "Cannot remove songs. Album is published."

            for song_to_rem in self.songs:
                if song_to_rem.name == song_name:
                    self.songs.remove(song_to_rem)
                    return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if not self.publish:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}"
        for the_song in self.songs:
            result += '\n' + f'== {the_song.get_info()}'
        return result
