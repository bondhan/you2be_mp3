from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'ignoreerrors': True,
    'quiet': True
}


playlist = 'https://www.youtube.com/playlist?list=PLYOnU0Yk8VGaR58T2MJjQ344qTtJ2V7Oo'

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    playlist_dict = ydl.extract_info(playlist, download=False)

    for video in playlist_dict['entries']:

        print()

        if not video:
            print('ERROR: Unable to get info. Continuing...')
            continue

        for property in ['thumbnail', 'id', 'title', 'description', 'duration']:
            print(property, '--', video.get(property))