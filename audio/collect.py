#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""collect.py

Collect data for testing 'perceived' audio quality

References
- https://www.quora.com/Is-there-an-objective-way-to-measure-sound-quality-Audio-community-often-cite-uneven-frequency-in-highs-mids-and-lows-as-poor-audio-quality-but-how-is-that-perceptually-negative-to-someone-who-listens-to-music?share=1
- http://www.bnoack.com/index.html?http&&&www.bnoack.com/audio/speech-level.html

Testing Standards
- PESQ: https://en.wikipedia.org/wiki/Perceptual_Evaluation_of_Speech_Quality
- POLQA: https://en.wikipedia.org/wiki/Perceptual_Objective_Listening_Quality_Analysis

Python Playing and Recording Sound
- https://realpython.com/playing-and-recording-sound-python/#recording-audio

"""

import simpleaudio as sa
import sounddevice as sd
import wave

from scipy.io.wavfile import write


def get_duration(filename):
    """Get wav file playback duration
    
    """
    with wave.open(filename, 'r') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


if __name__ == '__main__':
    import os
    import argparse


    PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    PARSER.add_argument("dir_in", help="Directory of input WAV files")
    PARSER.add_argument("dir_out", help="Directory of output WAV files")
    ARGS = PARSER.parse_args()


    # collect all absolute filenames from path
    filename_list = []
    for filename in os.listdir(ARGS.dir_in):
        path = os.path.join(ARGS.dir_in, filename)

        # filter-out non-functional files
        if not os.path.isfile(path):
            continue

        # filter-out undesired file-types
        if os.path.splitext(path)[1].lower() in (".wav"):
            filename_list.append(path)

    if not filename_list:
        sys.exit("[Error] Files not found: {}".format(ARGS.dir_in))


    # step through each file
    for file_speaker in filename_list:
        # construct output filename
        head, tail = os.path.split(file_speaker)
        file_listener = ARGS.dir_out + tail


        # play WAV file (speaker)
        print("Playing...")
        print(file_speaker)

        wave_obj = sa.WaveObject.from_wave_file(file_speaker)
        play_obj = wave_obj.play()


        # record WAV file (listener)
        print("Recording...")
        print(file_listener)

        fs = 44100 # sampling rate
        seconds = get_duration(file_speaker) + 1 # recording duration [sec]
        recording = sd.rec(int(round(seconds * fs)), samplerate=fs, channels=1)

        play_obj.wait_done() # wait until sound has finished playing
        sd.wait() # wait until recording is finished

        write(file_listener, fs, recording) # save as WAV file
