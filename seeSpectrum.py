import import scipy.fftpack
import matplotlib.pyplot as plt

def seeSpectrum(data, fs):
    n = len(signal)
    k = np.arange(n)
    T = float(n)/fs
    frq = k/T
    frq = frq[range(n/2)]
    Y = np.fft.rfft(signal)/n
    Y = Y[range(n/2)]
    
    plt.plot(frq, Y)
    plt.xlabel('Frequency in Hz')
    plt.ylabel('Normalized spectrum')
    
