"""
Emit random audio lure
Author: Ben McEwen
Date: 18/03/2021
Last Modified: 26/03/2021
"""

import random
import os
import wave
from os import path
import pyaudio


def add_audio(species, calltype, audio_file):
    # Create directory for new sound lure
    if path.exists('audio/{}/{}/'.format(species, calltype)):
        print('Directory already exists')
    else:
        os.makedirs('audio/{}/{}/'.format(species, calltype))
        print('Directory created')
    
    nd = 'audio/{}/{}/{}'.format(species, calltype, audio_file)
    os.rename(audio_file, nd)
    print('File added')


def select_lure(species=None, calltype=None, proximity=None, index=None):
    #Select audio lure from pool of possible lures returns directory of selected lure
    lure_index = None
    lure_dir = None

    print('Selecting Lure...')
    
    if species == None:
        species = random.choice(os.listdir('audio'))
        
    if calltype == None:
        calltype = random.choice(os.listdir('audio/' + species))
    
    audio = os.listdir('audio/{}/{}'.format(species, calltype))
    if len(audio) > 0:
        lure_index = random.choice(audio)[:-4]
        lure_dir = 'audio/{}/{}/{}.wav'.format(species, calltype, lure_index)
    else: 
        print('No audio files')

    print('Lure {} has been selected'.format(lure_index))

    return lure_dir, lure_index


def play_lure(lure):
    #Play the selected lure
    print('Playing audio lure...')

    filename = lure
    chunk = 1024  
    
    # Open the sound file 
    wf = wave.open(filename, 'rb')
    
    # Create an interface to PortAudio
    p = pyaudio.PyAudio()
    
    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    
    # Read data in chunks
    data = wf.readframes(chunk)
    
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)
        
    print('Audio lure has finished')
    
    # Close and terminate the stream
    stream.close()
    p.terminate()
    
#add_audio('wallaby', 'aggression', 'file.wav')
#lure_dir, index = select_lure()
#play_lure(lure_dir)




