import os
import librosa
import librosa.display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import IPython.display as ipdisplay

from pytube import YouTube
from os import path
from pydub import AudioSegment
from glob import glob
from IPython.core.display import display

from pedalboard import Pedalboard, Chorus, Reverb
from pedalboard.io import AudioFile

# Function to take video URL, convert to mp3, and download to desired location #
def download_mp3(url):

    yt = YouTube(str(url))
    print(f'\nDownloading {yt.title}...\n')

    # Download mp3 file if it doesn't exist already
    if not path.exists(yt.title + '.mp3'):
        video_to_audio = yt.streams.filter(only_audio=True).first()     # Convert from mp4 to mp3

        download_destination = '.'  #TODO: pass in destination path from function call and use here for download destination
        output_file = video_to_audio.download(output_path=download_destination)

        base_name, ext = path.splitext(output_file)
        new_file = base_name + '.mp3'

        os.rename(output_file, new_file)

        print('Track downloaded successfully.\n')

        return new_file

    else:
        print('MP3 file exists already.\n')


# Function to convert mp3 to wav format #
def mp3_to_wav(input_file):

    wav_file_name = 'track.wav'

    # Convert from mp3 to wav if it doesn't exist already
    if not path.exists(wav_file_name):

        to_reverse = input("Would you like the track to be reversed? (Y/N): ")

        if to_reverse == 'Y':
            segment_audio = AudioSegment.from_file(input_file).reverse()
        else:
            segment_audio = AudioSegment.from_file(input_file)

        segment_audio.export(wav_file_name, format='wav')
        print('\nConverted from mp3 to wav successfully.\n')

    else:
        print('\nWAV file exists already.\n')


def main():

    track_url = input('Input URL of track to download: ')

    mp3_filename = download_mp3(track_url)
    to_wav = input('Convert to WAV? (Y/N): ')

    # Ask if user wants to convert to wav format
    if to_wav == 'Y':
        mp3_to_wav(mp3_filename)

    # Read in the wav file frames and sample data
    with AudioFile('track.wav', 'r') as f:
        audio = f.read(f.frames)
        samplerate = f.samplerate

    # Begin adding effects to audio
    board = Pedalboard([Chorus(), Reverb(room_size=0.25)])
    effected = board(audio, samplerate)

    # Create a new file and write the audio file with changes
    with AudioFile('output.wav', 'w', samplerate, effected.shape[0]) as f:
        f.write(effected)


    #TODO: plot graphs for a better view of what's happening after the changes
    #audio_file = glob('track.wav')

    #y, sr = librosa.load('track.wav')

    #raw_graph = pd.Series(y).plot(figsize=(20, 10), lw=1, title='Raw audio data')
    #raw_graph.plot()
    #plt.show()

if __name__ == '__main__':
    main()

