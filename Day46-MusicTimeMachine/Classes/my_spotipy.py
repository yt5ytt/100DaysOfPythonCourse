import spotipy
import argparse
from spotipy.oauth2 import SpotifyOAuth

REDIRECT_URL = "http://localhost:5500/"


class MySpotipy:

    track_ids_list = []

    def __init__(self, spotipy_id, spotipy_secret, song_list, date):
        self.date = date
        self.spotipy_id = spotipy_id
        self.spotipy_secret = spotipy_secret
        self.song_list = song_list
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-public",
                redirect_uri=REDIRECT_URL,
                client_id=self.spotipy_id,
                client_secret=self.spotipy_secret,
                show_dialog=True,
                cache_path="token.json",
            )
        )
        self.user_id = self.user_auth()
        self.playlist = self.create_playlist()

    def user_auth(self):
        return self.sp.current_user()["id"]

    def get_track_ids(self, date, list_of_songs):
        """Gets list of songs and returns track ids"""
        song_uris = []
        year = date.split("-")[0]
        for song in list_of_songs:
            result = self.sp.search(q=f"track: {song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                continue
        return song_uris

    def create_playlist(self):
        """Creates playlist in users account"""
        return self.sp.user_playlist_create(user=self.user_id, name="Billboard Playlist", public=True)

    def import_songs_to_playlist(self):
        """Import songs into playlist from self.track_ids_list"""
        self.sp.playlist_add_items(playlist_id=self.playlist["id"], items=self.get_track_ids(self.date, self.song_list))


