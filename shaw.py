try:
  import spotipy
  from spotipy.oauth2 import SpotifyClientCredentials
  import pandas as pd
  import time
except ImportError:
  print("whoopsie")


# Connecting to spotify api - use this first 
client_id = "cfa82f8e94274193b3be3f646ed2ef96"
# Hush Hush
client_secret = "cb4e4456e93e471a8416f9c24c60e524"
cdm = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=cdm)


# Now down here you can start playing around
# Right lets try and get my artists
# My spotify name is Shaw Chifamba

"""
Retrieve Data from a specfic playlist
And then lets take a look at the energy of that playlist
"""
def GetSomeIDs(user, playlist_id):
  ids = []
  playlist = spotify.user_playlist(user, playlist_id)
    ids.append(album['id'])
  return ids

ids = GetSomeIDs('Shaw Chifamba', '13nuKjj1lmmDG6o7i51uc1')   
print(len(ids))
print(ids)

"""


"""






# Retrieve Artist Data
#artist_name = "{Post Malone}"
#search_result = spotify.search(artist_name)
#search_result['tracks']['items'][0]['artists']
#print(search_result)