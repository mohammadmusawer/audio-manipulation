import os

from pytube import YouTube
from os import path
from pydub import AudioSegment

# Function to take video URL, convert to mp3, and download to desired location #
def download_mp3(url):

    yt = YouTube(str(url))
    print(f'\nDownloading {yt.title}...\n')

    # Download mp3 file if it doesn't exist already
    if not path.exists(yt.title + '.mp3'):
        video_to_audio = yt.streams.filter(only_audio=True).first()     # Convert from mp4 to mp3
        download_destination = '.'
        output_file = video_to_audio.download(output_path=download_destination)

        base, ext = path.splitext(output_file)
        new_file = base + '.mp3'

        os.rename(output_file, new_file)

        print('Track downloaded successfully.\n')
        return new_file

    else:
        print('MP3 file exists already.\n')


# Function to convert mp3 to wav format #
def mp3_to_wav(input_file):

    wav_file_name = 'temp.wav'

    # Convert from mp3 to wav if it doesn't exist already
    if not path.exists(wav_file_name):
        segment_audio = AudioSegment.from_file(input_file)
        segment_audio.export(wav_file_name, format='wav')
        print('\nConverted from mp3 to wav successfully\n')
    else:
        print('\nWAV file exists already.\n')


def main():

    track_url = input('Input URL of track to download: ')

    mp3_filename = download_mp3(track_url)
    to_wav = input('Convert to WAV? (Y/N): ')

    # Ask if user wants to convert to mp3
    if to_wav == 'Y':
        mp3_to_wav(mp3_filename)
    else:
        exit(1)


if __name__ == '__main__':
    main()

