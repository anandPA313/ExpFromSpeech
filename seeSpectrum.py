import scipy.fftpack
import matplotlib.pyplot as plt

# Function to plot FFT of any signal time domain.

def seeSpectrum(data, fs):
# Signal - the time domain sequence
# fs     - the sampling frequency of the signal
    
    n = len(signal)
    k = np.arange(n)
    T = float(n)/fs
    
    # Get the frequency values
    frq = k/T       
    
    # We want only real spectrum
    frq = frq[range(n/2)]
    
    # Compute normalized FFT
    Y = np.fft.rfft(signal)/n
    
    # Real part
    Y = Y[range(n/2)]
    
    # Plot and see
    plt.plot(frq, Y)
    plt.xlabel('Frequency in Hz')
    plt.ylabel('Normalized spectrum')
    
