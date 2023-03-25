import numpy as np
import matplotlib.pyplot as plt

# Define the function to fit
def gaussian(x, a, x0, sigma, b):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2)) + b

# Generate a simulated blazar light curve with n flares
t = np.linspace(0, 1000, 1000)
y_true = np.zeros_like(t)
yerr = 0.1*np.ones_like(y_true)
np.random.seed(42)
for i in range(8): #n
    t0 = np.random.uniform(20,980)
    a = np.random.uniform(1, 6)
    sigma = np.random.uniform(12, 50)
    y_true += gaussian(t, a, t0, sigma, 0)
y_obs = y_true + yerr*np.random.randn(len(y_true))

plt.errorbar(t, y_obs, yerr=yerr, fmt='.', label='Observed')
plt.plot(t, y_true, label='True')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Flux')
plt.show()
