# -*- coding: utf-8 -*-
# @Author: orres
# @Email:  jasonjin22@gmail.com
# @Date:   2019-03-21 00:25:35
# @Last Modified by:   orres
# @Last Modified time: 2019-03-21 10:40:37
# This is a simulating program of TOFEL speaking section(especially for part one and two)
# The topics in the "tofel speaking 80.txt" is collected from the internet

import pyaudio
import wave

def get_audio(filepath):
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 11025
    RECORD_SECONDS = 45
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print(50*"*", "finished\n")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


 





