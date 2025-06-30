import numpy as np

# Set constants
k = 1.38e-23 # Boltzmann constant in J/K
q = 1.602e-19 # Charge of an electron in C
T = 300 # Temperature K
R = 50e3 # Resistance across detector in ohms (typical range 10-100 kohms)
l = 638e-9 # Wavelength in nm
h = 6.626e-34 # Planck's constant in J*s
c = 3e8 # Speed of light in m/s
A = 1e-20 # 1/f constant in A^2/Hz (typical range 10^-24-10^-18 A^2/Hz)
P_o = 2e-9 # Laser optical power at ground in W (from link budget)
T = 32e-6 # Integration time
B = 1/(2 * T) # Bandwidth in Hz
f_l = B/10 # Lower cutoff frequency in Hz

# Camera specfic constants
# ASI1600

n = 0.6 # Quantum efficiency at 638nm (unitless)
f_s = 15 # Sampling frequency in Hz
R_l = q*l*n/(h*c) # Responsivity of detector in A/W
i_ph = R_l * P_o # Photocurrent in detector in A

# Define the noise current for each source
I_t2 = 4*k*T*B/R # Thermal noise
I_s2 = 2*q*i_ph*B # Shot noise
I_f2 = A * np.log(1+(B/f_l)) # 1/f noise

# Combine
I_n = I_t2 + I_s2 + I_f2 # Mean square noise

print("Below are the specs for the ASI1600 Camera:")
print(f"RMS thermal noise: {np.sqrt(I_t2)*1e6} muA")
print(f"RMS shot noise: {np.sqrt(I_s2)*1e6} muA")
print(f"RMS 1/f noise: {np.sqrt(I_f2)*1e6} muA")
print(f"RMS total noise: {np.sqrt(I_n)*1e6} muA")
print(f"Responsivity: {R_l} A/W")
print(f"Photocurrent: {i_ph} A")

# Compute SNR
SNR = i_ph**2/I_n
SNR_dB = 10*np.log10(SNR)

print(f"Linear SNR: {SNR}")
print(f"SNR in dB: {SNR_dB}")
print()

# ASI585MM Pro

n = 0.91 # Quantum efficiency at 638nm (unitless)
f_s = 47 # Sampling frequency in Hz
R_l = q*l*n/(h*c) # Responsivity of detector in A/W
i_ph = R_l * P_o # Photocurrent in detector in A

# Define the noise current for each source
I_t2 = 4*k*T*B/R # Thermal noise
I_s2 = 2*q*i_ph*B # Shot noise
I_f2 = A * np.log(1+(B/f_l)) # 1/f noise

# Combine
I_n = I_t2 + I_s2 + I_f2 # Mean square noise

print("Below are the specs for the ASI585MM Pro Camera:")
print(f"RMS thermal noise: {np.sqrt(I_t2)*1e6} muA")
print(f"RMS shot noise: {np.sqrt(I_s2)*1e6} muA")
print(f"RMS 1/f noise: {np.sqrt(I_f2)*1e6} muA")
print(f"RMS total noise: {np.sqrt(I_n)*1e6} muA")
print(f"Responsivity: {R_l} A/W")
print(f"Photocurrent: {i_ph} A")

# Compute SNR
SNR = i_ph**2/I_n
SNR_dB = 10*np.log10(SNR)

print(f"Linear SNR: {SNR}")
print(f"SNR in dB: {SNR_dB}")
print()

# ASI432

n = 0.79 # Quantum efficiency at 638nm (unitless)
f_s = 120 # Sampling frequency in Hz
R_l = q*l*n/(h*c) # Responsivity of detector in A/W
i_ph = R_l * P_o # Photocurrent in detector in A

# Define the noise current for each source
I_t2 = 4*k*T*B/R # Thermal noise
I_s2 = 2*q*i_ph*B # Shot noise
I_f2 = A * np.log(1+(B/f_l)) # 1/f noise

# Combine
I_n = I_t2 + I_s2 + I_f2 # Mean square noise

print("Below are the specs for the ASI1600 Camera:")
print(f"RMS thermal noise: {np.sqrt(I_t2)*1e6} muA")
print(f"RMS shot noise: {np.sqrt(I_s2)*1e6} muA")
print(f"RMS 1/f noise: {np.sqrt(I_f2)*1e6} muA")
print(f"RMS total noise: {np.sqrt(I_n)*1e6} muA")
print(f"Responsivity: {R_l} A/W")
print(f"Photocurrent: {i_ph} A")

# Compute SNR
SNR = i_ph**2/I_n
SNR_dB = 10*np.log10(SNR)

print(f"Linear SNR: {SNR}")
print(f"SNR in dB: {SNR_dB}")
