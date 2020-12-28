#!/usr/local/bin/python3
''' 
Convert json output from deepspeech into formatted text file for mi-diaries project
Author: Matt Churgin (mattchurgin@gmail.com), Dec 2020
'''
import json
import argparse

def parse_json(j, utterance_chunk=10): 
    '''
    Parse deepspeech json output to desired format:
    Utterance_1 Starttime Endtime
    Utterance_2 Starttime Endtime
    etc.

    Inputs: 
        1) j: json object 
        2) utterance_chunk: Duration (s) of utterances to segment the output into
    '''
    raw_words = j['transcripts'][0]['words'] 
    parsed = [] 
    i = 0 
    while i < len(raw_words): 
        if i==0:
            abs_start_time = raw_words[i]['start_time'] 
        else:
            abs_start_time = abs_end_time
        rel_end_time = 0
        to_print = raw_words[i]['word'] 
        j=i 
        while rel_end_time < utterance_chunk: 
           if j<len(raw_words)-1: 
               j+=1 
           else: 
               break     
           to_print += ' ' + raw_words[j]['word'] 
           rel_end_time = raw_words[j]['start_time'] + raw_words[j]['duration'] - abs_start_time 
        
        abs_end_time = raw_words[j]['start_time'] + raw_words[j]['duration'] 
        to_print += ' ' + str(abs_start_time) + ' ' + str(abs_end_time) 
        #print(to_print) 
        parsed.append(to_print) 
         
        #abs_start_time = raw_words[j]['start_time'] 
        i = j+1 
         
    return parsed 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input json file to parse", required=True)
    parser.add_argument("-o", "--output", help="filename to save parsed text", required=True)
    args = parser.parse_args()

    input_json = args.input
    outfile = args.output

    with open(input_json) as f:
        raw_json = json.load(f)
    
    parsed = parse_json(raw_json)

    parsed = '\n'.join(parsed)
    with open(outfile, 'w') as f:
        f.write(parsed)
