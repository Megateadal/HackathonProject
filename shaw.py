import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ['SPOTIPY_CLIENT_ID'] = 'cfa82f8e94274193b3be3f646ed2ef96'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'cb4e4456e93e471a8416f9c24c60e524'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://www.google.com/'

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
playlists = sp.user_playlists('ShawChifamba')
print(playlists['total'])


def get_playlists(sp):
    global playlists
    playlist_uri = []

    for playlist in playlists['items']:
        print(sp.playlist_tracks(playlist['uri']))
        

get_playlists(sp)



# while playlists:
# for i, playlist in enumerate(playlists['items']):
#     print(f"URL: {playlist['uri']} NAME: {playlist['name']} TOTAL: ")
# if playlists['next']:
#     playlists = sp.next(playlists)
# else:
#     playlists = None
