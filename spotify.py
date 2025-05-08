import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Credentials
SPOTIPY_CLIENT_ID = "YOUR CLIENT ID"
SPOTIPY_CLIENT_SECRET = "YOUR SECRET ID"
SPOTIPY_REDIRECT_URI = "YOUR URL CALLBACK"

# Inisialisasi autentikasi Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-public"
))

# ID Playlist Spotify
PLAYLIST_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def read_playlist_file(filepath):
    track_names = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ' - ' in line:
                track_names.append(line)
    return track_names


def search_track(track_name):
    results = sp.search(q=track_name, limit=1, type='track')
    if results and results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track['id']
    else:
        return None


def get_existing_tracks():
    existing_tracks = set()
    results = sp.playlist_tracks(PLAYLIST_ID)
    
    while results:
        for item in results['items']:
            track = item['track']
            if track:
                existing_tracks.add(track['id'])
        results = sp.next(results) if results['next'] else None

    return existing_tracks


def add_tracks_by_name(track_names):
    existing_tracks = get_existing_tracks()
    new_tracks = []

    for track_name in track_names:
        track_id = search_track(track_name)
        if track_id and track_id not in existing_tracks:
            new_tracks.append(track_id)

    if not new_tracks:
        return

    batch_size = 100
    total_added = 0

    for i in range(0, len(new_tracks), batch_size):
        batch = new_tracks[i:i + batch_size]
        try:
            sp.playlist_add_items(PLAYLIST_ID, batch)
            total_added += len(batch)
        except spotipy.exceptions.SpotifyException as e:
            print(f"Gagal menambahkan batch: {e}")


def main():
    file_path = "YOUR FILEPATH NAME with TXT Files"
    track_names = read_playlist_file(file_path)
    add_tracks_by_name(track_names)


if __name__ == "__main__":
    main()



#example for TXT format

#Running with the Wild Things - Against The Current
#Dreaming Alone - Against The Current ft Taka from ONE OK ROCK