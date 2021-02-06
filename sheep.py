try:
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    import pandas as pd
    import time
except ImportError:
    print("whoopsie")

# Connecting to spotify api
client_id = "cfa82f8e94274193b3be3f646ed2ef96"

client_secret = "cb4e4456e93e471a8416f9c24c60e524"
cdm = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=cdm)

print("running sheep code")
"""birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])"""

"""#Glass Animals top 10 tracks with image urls
ga_uri = "spotify:artist:4yvcSjfu4PC0CYQyLy4wSq"
results = spotify.artist_top_tracks(ga_uri)

for track in results['tracks'][:10]:
    print('track: ' + track['name'])
    #print('audio: ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
    
"""
sheepName = "Cynical__Sheep"
sheepID = "kgfedpw2w8mxtw2euccx1vt36"

#Glass Animals album names
ga_uri = "spotify:artist:4yvcSjfu4PC0CYQyLy4wSq"
results = spotify.artist_albums(ga_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
