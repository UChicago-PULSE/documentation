import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34 # Planck's constant J*s
c = 3e8 # Speed of light m/s
l = 638e-9 # Wavelength of incoming light m
P_1 = 1.7e-9 # Good optical power W (from link budget with transmit power 0.1 W)
P_2 = 1.91e-12 # Bad optical power W (from link budget with transmit power 23 dBm)

# Define a range of exposure times
t = np.linspace(1e-3,1e-1,500)

# Compute photons per pixel
N = 20*20 # Number of pixels hit by the beam
mu_p1 = P_1*t/(h*c/l)/N # Mean photons received per pixel
mu_p2 = P_2*t/(h*c/l)/N # Mean photons received per pixel

# QE for each camera at wavelength 638nm
QE1 = 0.8
QE2 = 0.83
QE3 = 0.95

# Dark noise (e/s/pix * exposure time)
DN = 0.5*t # Upper bound for ASI1600 and ASI585MM Pro, just assume it's the same for ASI432

# Quantization noise
QN = 1/12 # DN^2

# Overall system gain (DN/e-)
K1 = 1/0.5
K2 = 1/1
K3 = 1/5

# Compute SNR
def SNR(x,y):
    return x/np.sqrt(DN+(QN/y)+x)

SNR11 = SNR(QE1*mu_p1, K1)
SNR21 = SNR(QE2*mu_p1, K2)
SNR31 = SNR(QE3*mu_p1, K3)

SNR12 = SNR(QE1*mu_p2, K1)
SNR22 = SNR(QE2*mu_p2, K2)
SNR32 = SNR(QE3*mu_p2, K3)

def dB(x):
    return 10*np.log10(x)

SNR_dB11 = dB(SNR11)
SNR_dB21 = dB(SNR21)
SNR_dB31 = dB(SNR31)

SNR_dB12 = dB(SNR12)
SNR_dB22 = dB(SNR22)
SNR_dB32 = dB(SNR32)

# Make the plot
plt.figure(figsize=(8,7))
plt.plot(t, SNR_dB11, label="Strong ASI1600")
plt.plot(t, SNR_dB21, label="Strong ASI585MM Pro")
plt.plot(t, SNR_dB31, label="Strong ASI432")
plt.plot(t, SNR_dB12, linestyle=':', label="Weak ASI1600")
plt.plot(t, SNR_dB22, linestyle=':', label="Weak ASI585MM Pro")
plt.plot(t, SNR_dB32, linestyle=':', label="Weak ASI432")
plt.title(r"SNR$=10\log_{10}\left(\frac{\eta \mu_p}{\sqrt{\sigma_d^2+\sigma_q^2/K+\eta\mu_p}}\right)$ vs. exposure time")
plt.xlabel("Time (s)")
plt.ylabel("SNR (dB)")
plt.grid(True)
plt.legend()
plt.show()