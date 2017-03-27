from numpy import argmax, diff
from matplotlib.mlab import find
from scipy.signal import fftconvolve
import sys
import wave
import struct
import numpy as np
import math
import matplotlib.pyplot as plt


def freq_from_autocorr(sig, fs):

    # Find out autocorerlation of the frame
    corr = fftconvolve(sig, sig[::-1], mode='full')
    
    # We're not interested in negative delays. NOTE // returns integer after division
    corr = corr[len(corr)//2:]

    # Find the first peak
    d = diff(corr)
    start = find(d > 0)[0]
    
    # Next peak
    peak = argmax(corr[start:]) + start

    # Convert it to freq and return.
    return float(fs) / peak



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

    # wavPath = sys.argv[1]
    # Or if you prefer, specify the sound file path here.
    wavPath = './bloomingdales1.wav'

    # Pitch values will be stores in this file
    OUTFILE = './pitch.txt'

    x, fs, length = readWav(wavPath)

    # Getting the time values.
    t = np.arange(start=float(1)/fs,stop=float(length)/fs,step=float(1)/fs)

    windowSize = 20e-3
    shiftSize = 10e-3
    endVal = t[-1]

    nShifts = math.floor((endVal-windowSize)/shiftSize)
    startTime = 0; endTime = windowSize
    pitch = []; time = []
    for i in range(0,int(nShifts)):

        # We have start and end time for this window.
        # We need start and end indices for this window so that
        # we can get the frame corresponding to the timings.
        for kk in range(0,len(t)):
            if t[kk]>startTime:
                startIdx = kk
                break
        for kk in range(0,len(t)):
            if t[kk]>endTime:
                endIdx = kk-1
                break
        frame = x[0][startIdx:endIdx]       # Got the frame

        # Get the fundamental freq for this frame
        pitchFrame = freq_from_autocorr(frame, fs)

        # Add the new value
        pitch.append(pitchFrame)
        time.append(startTime)

        # Move the window 10 ms towards the right
        startTime = startTime+shiftSize
        endTime = endTime+shiftSize

    # Plot the values
    plt.plot(time, pitch)
    plt.ylabel('Hz'); plt.xlabel('seconds')
    plt.show()

    # Save the results.
    np.savetxt(OUTFILE, zip(time, pitch), fmt='%.4f')
