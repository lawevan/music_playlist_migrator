from music_playlist_migrator.Playlists import Spotify, YTMusic

if __name__ == '__main__':
    playlist = Spotify("My Playlist")
    ytplaylist = YTMusic("My Playlist")

    print(playlist)  # When the track list is empty
    playlist.tracks = ["Song 1", "Song 2", "Song 3"]
    print(playlist)

    print(ytplaylist)  # When the track list is empty
    ytplaylist.tracks = ["Song 1", "Song 2", "Song 3"]
    print(ytplaylist)