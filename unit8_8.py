def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('Atif', 'Tiger')
print(album)

album = make_album('Arjit', 'villan')
print(album)

album = make_album('Mohit', 'Berfi')
print(album)

album = make_album('Shan', 'newyear', tracks=8)
print(album)