def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('Atif', 'Tiger')
print(album)

album = make_album('Arjit', 'villan')
print(album)

album = make_album('Shan', 'newyear')
print(album)