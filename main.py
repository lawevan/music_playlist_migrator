from music_playlist_migrator.Spotify import Spotify

if __name__ == '__main__':
    playlist = Spotify("My Playlist")
    print(playlist)  # When the track list is empty
    playlist.tracks = ["Song 1", "Song 2", "Song 3"]

    print(playlist)
