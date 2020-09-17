#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Single-Tone Generator

import pygame, pygame.sndarray
import numpy
import scipy.signal


SAMPLE_RATE = 44100 # [Hz]

# https://stackoverflow.com/questions/56592522/python-simple-audio-tone-generator
pygame.mixer.pre_init(frequency=SAMPLE_RATE, size=-16, channels=1, buffer=1024)
pygame.init()


def play_for(sample_wave, ms):
    """Play the given NumPy array, as a sound, for ms milliseconds."""
    sound = pygame.sndarray.make_sound(sample_wave)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()


def sine_wave(frequency, amplitude, n_samples=SAMPLE_RATE):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    length = SAMPLE_RATE / float(frequency)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = amplitude * numpy.sin(xvalues)
    return numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)


# @TODO: Returns error
# def square_wave(frequency, amplitude, duty_cycle=.5, n_samples=SAMPLE_RATE):
#     """Compute N samples of a sine wave with given frequency and peak amplitude.
#        Defaults to one second.
#     """
#     t = numpy.linspace(0, 1, 500 * int(round(440/frequency)), endpoint=False)
#     wave = scipy.signal.square(2 * numpy.pi * 5 * t, duty=duty_cycle)
#     wave = numpy.resize(wave, (n_samples,))
#     return (amplitude / 2 * wave.astype(numpy.int16))


if __name__ == '__main__':
    import argparse

    PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    PARSER.add_argument("freq", help="Tone frequency [Hz]")
    PARSER.add_argument("duration", help="Tone duration [sec]")
    ARGS = PARSER.parse_args()

    # play single tone
    play_for(sine_wave(int(ARGS.freq), 4096), int(ARGS.duration) * 1000)
