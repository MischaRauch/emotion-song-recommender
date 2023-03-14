import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Ele's client ID
client_id = '6e1a09c940a943da95144c6f49a0717b'
client_secret = 'ccc2af43075641f9899eaaac5b716b8b'


def authenticate(client_id, client_secret):
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


def get_playlist_URI(sp, query):
    results = sp.search(q=query, type='playlist', limit=10)
    playlist_uri = results['playlists']['items'][0]['uri']
    return playlist_uri


# maximum of songs is 100
def get_songs(sp, number_of_songs, playlist_uri):
    playlist = sp.playlist(playlist_uri)
    songs = playlist['tracks']['items'][:number_of_songs]
    return songs


def create_table_songs(sp, songs):
    tracks = []
    for song in songs:
        track = song['track']
        id = track['id']
        features = sp.audio_features(id)
        name = track['name']
        album = track['album']['name']
        artist = track['album']['artists'][0]['name']
        release_date = track['album']['release_date']
        length = track['duration_ms']
        popularity = track['popularity']
        acousticness = features[0]['acousticness']
        danceability = features[0]['danceability']
        energy = features[0]['energy']
        instrumentalness = features[0]['instrumentalness']
        liveness = features[0]['liveness']
        valence = features[0]['valence']
        loudness = features[0]['loudness']
        speechiness = features[0]['speechiness']
        tempo = features[0]['tempo']
        key = features[0]['key']
        time_signature = features[0]['time_signature']
        tracks.append([id, name, album, artist, release_date, popularity, length, danceability, acousticness,
                       energy, instrumentalness, liveness, valence, loudness, speechiness, tempo, key, time_signature])
    columns = ['id', 'name', 'album', 'artist', 'release_date', 'popularity', 'length', 'danceability', 'acousticness',
               'energy', 'instrumentalness',
               'liveness', 'valence', 'loudness', 'speechiness', 'tempo', 'key', 'time_signature']

    return pd.DataFrame(tracks, columns=columns)


# test
sp = authenticate(client_id, client_secret)
songs = get_songs(sp, 100, get_playlist_URI(sp, 'happy'))
data = create_table_songs(sp, songs)
