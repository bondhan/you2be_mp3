ydl_opts = {
    'ignoreerrors': True,
    'quiet': True
}

input_file = open("url")

for playlist in input_file:

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        playlist_dict = ydl.extract_info(playlist, download=False)

        for video in playlist_dict['entries']:

            print()

            if not video:
                print('ERROR: Unable to get info. Continuing...')
                continue

            for property in ['thumbnail', 'id', 'title', 'description', 'duration']:
                print(property, '--', video.get(property))