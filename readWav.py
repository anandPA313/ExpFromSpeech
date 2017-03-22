# Python code to read a wave file (.wav format)

import wave
import struct
import numpy as np

def readWav(path):
  
    waveFile = wave.open(wavPath)
    fs = waveFile.getframerate()
    length = waveFile.getnframes()
    data = []
    for i in range(0, length):
        waveData = waveFile.readframes(1)
        data.append(struct.unpack("<h", waveData))
    waveFile.close()
    data = np.array([data])
    data = data.astype(float)/np.max(np.abs(data))
    data = data[0].T
    return data, fs, length
  
  
  if __name__ == "__main__":
    
    # Usage: $python readWav.py 'inputSpeech.wav'
    
    wavPath = sys.argv[1]
    x, fs, length = readWav(wavPath)
    
