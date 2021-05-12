"""
Get Recording using Respeaker Array V2.0
Author: Ben McEwen
Date: 18/03/2021

"""

import wave
import numpy as np
import datetime
import pyaudio
from lure import select_lure
from doa import direction

 
RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 6 
RESPEAKER_WIDTH = 2
RESPEAKER_INDEX = 1  # Run get_index.py to find the index for your device
CHUNK = 1024
RECORD_SECONDS = 5



def filename(location, index):
    x = datetime.datetime.now()
    date = x.strftime("%d%m%y")
    time = x.strftime("%H%M%S")

    FILENAME = '/home/pi/Audio-Lure/recordings/{}-{}-{}-{}.wav'.format(location, index, date, time)
    FILENAME_DATA = '/home/pi/Audio-Lure/recordings/{}-{}-{}-{}-DOA.csv'.format(location, index, date, time)

    print('Files created')
    return FILENAME, FILENAME_DATA



def record(FILENAME, FILENAME_DATA):
    frames = [] 
    DOA = []
    time = []

    p = pyaudio.PyAudio()

    print('Recording...')

    stream = p.open(
                rate=RESPEAKER_RATE,
                format=p.get_format_from_width(RESPEAKER_WIDTH),
                channels=RESPEAKER_CHANNELS,
                input=True,
                input_device_index=RESPEAKER_INDEX,)
    
    for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        a = np.fromstring(data,dtype=np.int16)[0::6]
        frames.append(a.tostring())
        x = datetime.datetime.now()
        time.append(x.strftime('%M:%S'))
        DOA.append(str(direction()))

    data = np.array([DOA, time])
    data = data.T

    stream.stop_stream()
    stream.close()
    p.terminate()

    print('Finished recording, saving data')
    
    wf = wave.open(FILENAME, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return DOA

