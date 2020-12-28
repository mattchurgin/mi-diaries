#!/bin/sh
# 1: input audio file to convert

echo "Running text-to-speech with deepspeech:"
echo "$(date)"
echo "======================="

input="$1"

file_created=$(date -r "$input" +%F)
full_date_str="$file_created"
pathtofile=`dirname "$input"`
filename=`basename "$input"`
fname="${filename%.*}"
fname_new="${fname// /_}"_${full_date_str}

wav_input="${fname_new}.wav"

echo "Coverting file to .wav"
echo "======================="
ffmpeg -i "${input}" "${wav_input}"

#echo $wav_input

ds_out="output.json"

parsed_out="${fname// /_}"_${full_date_str}.txt
#echo $parsed_out

echo "Running deepspeech"
deepspeech --model deepspeech-0.9.3-models.pbmm \
--scorer deepspeech-0.9.3-models.scorer \
--candidate_transcripts 1 \
--json \
--audio $wav_input \
> $ds_out
echo "deepspeech STT complete"

echo "Parsing deepspeech"
python tts_ds.py -i $ds_out -o $parsed_out

echo "Done"