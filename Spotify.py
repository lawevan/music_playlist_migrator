class Spotify:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.tracks = []

    def __str__(self):
        track_str = ', '.join([str(track) for track in self.tracks])
        return f"Playlist: {self.playlist_id}\nTracks: {track_str}"
