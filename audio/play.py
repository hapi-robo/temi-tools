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
import time


if __name__ == '__main__':
    import os
    import argparse


    PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    PARSER.add_argument("dir", help="Directory of input WAV files")
    ARGS = PARSER.parse_args()


    # collect all absolute filenames from path
    filename_list = []
    for filename in os.listdir(ARGS.dir):
        path = os.path.join(ARGS.dir, filename)

        # filter-out non-functional files
        if not os.path.isfile(path):
            continue

        # filter-out undesired file-types
        if os.path.splitext(path)[1].lower() in (".wav"):
            filename_list.append(path)

    if not filename_list:
        sys.exit("[Error] Files not found: {}".format(ARGS.dir))


    # play each WAV file
    for filename in filename_list:
        print(filename)

        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()

        time.sleep(3);