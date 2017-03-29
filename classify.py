import numpy as np
from sklearn.svm import SVC
import os



pitchDir = './pitch/'
files = os.listdir(pitchDir)

def readFiles(files):

    anger = []; neutral = []
    for i in range(0,len(files)/2):
        fileName = files[i]
        t,data = np.loadtxt(pitchDir+fileName, unpack=True)
        anger.append(np.ndarray.tolist(data))
    for i in range(len(files)/2,len(files)):
        fileName = files[i]
        t, data = np.loadtxt(pitchDir+fileName, unpack=True)
        neutral.append(np.ndarray.tolist(data))
    return neutral, anger



if __name__ == "__main__":

    neutral_samples, anger_samples = readFiles(files)
    k=0
