#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Linear Frequency Sweep Tone Generator

from tone import play_for, sine_wave

if __name__ == '__main__':
    import argparse

    PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    PARSER.add_argument("start", help="Start tone frequency [Hz]")
    PARSER.add_argument("end", help="End tone frequency [Hz]")
    PARSER.add_argument("inc", help="Increment tone frequency [Hz]")
    PARSER.add_argument("duration", help="Tone duration [sec]")
    ARGS = PARSER.parse_args()

    # linearly sweep
    for freq in range(int(ARGS.start), int(ARGS.end), int(ARGS.inc)):
        print("Frequency: {} Hz".format(freq))
        play_for(sine_wave(int(freq), 4096), int(ARGS.duration) * 1000)
