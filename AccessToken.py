import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = '5ee7a648878b46cfb5f4c973736acc99'
CLIENT_SECRET = 'ff39b32792fa4603b830accb294bf433'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []

for i in range(0,50,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

    import pandas as pd

    track_dataframe = pd.DataFrame(
        {'artist_name': artist_name, 'track_name': track_name, 'track_id': track_id, 'popularity': popularity})
    print(track_dataframe)
    track_dataframe.head()