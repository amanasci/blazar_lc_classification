import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

k = 10000

# Define the flare function
def flare(t, f_c, f_0, t_0, t_r, t_d):
    return f_c + f_0 / ((np.exp((t_0 - t) / t_r)) + (np.exp((t - t_0) / t_d)))

# Generate a simulated blazar light curve with six flares
t = np.linspace(0, 100, k)
y_true = np.zeros_like(t)
yerr = 0.1*np.ones_like(y_true)

for i in range(5):
    t0 = np.random.uniform(20, 80)
    f_0 = np.random.uniform(1, 3)
    t_r = np.random.uniform(2, 5)
    t_d = np.random.uniform(2, 5)
    y_true += flare(t, 0, f_0, t0, t_r, t_d)
y_obs = y_true + yerr*np.random.randn(len(y_true))

plt.plot(t,y_obs)