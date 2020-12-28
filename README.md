# mi-diaries
On-prem speech-to-text pipeline for mi-diaries project

Convert individual audio files to text with timestamps. Uses deepspeech (cpu version currently). See [here](https://deepspeech.readthedocs.io/en/latest/index.html) for more info on setting up deepspeech.

## Installation
1) pip3 install -r requirements.txt
2) Requires ffmpeg and sox
3) Requires pre-trained model and scorer. Download from the following links:
* https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
* https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

## Usage
1) All scripts, the pre-trained model and scorer should be located in the same directory. 
2) Run the shell script with the audio file to convert as a command line argument, as shown below.
```
./tts_ds.sh path/to/audio_file
```
3) Formatted speech-to-text file will be written to the working directory.


