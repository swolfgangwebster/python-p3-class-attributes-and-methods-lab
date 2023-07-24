class Song:

    count = 0

    def __init__(self,n,a,g):
        self.name = n
        self.artist = a
        self.genre = g
        Song.add_song_to_count()
        Song.add_to_genres(g)
        Song.add_to_artists(a)

    def add_song_to_count():
        Song.count += 1

    genres = []
    genre_count = {}

    def add_to_genres(g):
        if g not in Song.genres:
            Song.genres += [g]
            Song.genre_count[g] = 0
        Song.genre_count[g] += 1

    artists = []
    artist_count = {}

    def add_to_artists(a):
        if a not in Song.artists:
            Song.artists += [a]
            Song.artist_count[a] = 0
        Song.artist_count[a] += 1
        
        