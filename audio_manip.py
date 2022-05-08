import os
from pytube import YouTube
from os import path

def main():
    track_url = input('Input URL of track to download: ')
    yt = YouTube(str(track_url))

    print(f'Downloading {yt.title}...')

    # Convert video to audio (mp3)
    video_to_audio = yt.streams.filter(only_audio=True).first()

    download_destination = '.'

    output_file = video_to_audio.download(output_path=download_destination)

    base, ext = path.splitext(output_file)
    new_file = base + '.mp3'
    os.rename(output_file, new_file)

    print('Downloaded track successfully.')


if __name__ == '__main__':
    main()