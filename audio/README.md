# Microphone Audio Tests

## Frequency Bands of Interest
* Vowels: 250 - 500 Hz
* Consonants: 2000 - 4000 Hz


## Volume Settings
Make sure `Over-Amplification` is turned off (`Settings` > `Sound`)
```
amixer -D pulse sset Master 35%
```

## References
- [Audio Check](https://www.audiocheck.net/index.php)
- [Audio Test Signals](https://www.genelec.com/audio-test-signals)
- [Is there an objective way to measure sound quality?](https://www.quora.com/Is-there-an-objective-way-to-measure-sound-quality-Audio-community-often-cite-uneven-frequency-in-highs-mids-and-lows-as-poor-audio-quality-but-how-is-that-perceptually-negative-to-someone-who-listens-to-music)
- [Human Speech Levels](http://www.bnoack.com/index.html?http&&&www.bnoack.com/audio/speech-level.html)
- Testing Standards
	- [PESQ](https://en.wikipedia.org/wiki/Perceptual_Evaluation_of_Speech_Quality)
	- [POLQA](https://en.wikipedia.org/wiki/Perceptual_Objective_Listening_Quality_Analysis)
- [Python Playing and Recording Sound](https://realpython.com/playing-and-recording-sound-python/#recording-audio)