class Spotify:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.tracks = []

    def __str__(self):
        track_str = ', '.join([str(track) for track in self.tracks])
        return f"Spotify Playlist: {self.playlist_id}\nTracks: {track_str}"


class YTMusic:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.tracks = []

    def __str__(self):
        track_str = ', '.join([str(track) for track in self.tracks])
        return (f"YouTube Music Playlist: {self.playlist_id}\n"
                f"Tracks: {track_str}")
