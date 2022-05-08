import os

from pytube import YouTube
from os import path
from pydub import AudioSegment

# Function to take video URL, convert to mp3, and download to desired location #
def download_mp3(url):

    yt = YouTube(str(url))
    print(f'Downloading {yt.title}...')

    video_to_audio = yt.streams.filter(only_audio=True).first()
    download_destination = ''

    output_file = video_to_audio.download(output_path=download_destination)

    #TODO: Check for mp3 file to make sure it downloaded successfully by checking .mp3 file exists
    print('Track downloaded successfully.')

    return output_file

# Function to convert mp3 to wav format #
def mp3_to_wav(input_file):
    segment_audio = AudioSegment.from_file(input_file)
    segment_audio.export('temp.wav', format='wav')

    #TODO: check if conversion was done successfully by checking if .wav file exists
    print('Converted from mp3 to wav successfully\n')


def main():
    track_url = input('Input URL of track to download: \n')
    downloaded_file = download_mp3(track_url)

    base, ext = path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)

    to_wav = input("Convert to WAV? (Y/N): \n")

    if to_wav == 'Y':
        mp3_to_wav(new_file)
    else:
        exit(1)


if __name__ == '__main__':
    main()
