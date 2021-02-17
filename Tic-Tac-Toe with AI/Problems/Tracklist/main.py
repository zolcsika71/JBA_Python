def tracklist(**tracks):
    for track in tracks:
        print(track)
        for album in tracks[track]:
            print(f'ALBUM: {album} TRACK: {tracks[track][album]}')






