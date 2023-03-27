import numpy as np
import matplotlib.pyplot as plt

"""
Simulating blazar light curves using a simple stochastic process called the Ornstein-Uhlenbeck (OU) process
"""


# Set simulation parameters
timestep = 0.1  # Time step (days)
total_time = 1000  # Total simulation time (days)
num_simulations = 5  # Number of light curve simulations to generate

# Set OU process parameters
tau = 20  # Decay time scale (days)
sigma = 0.1  # Fluctuation amplitude (Jy)

# Define OU process function
def ou_process(tau, sigma, total_time, timestep):
    # Initialize variables
    t = np.arange(0, total_time, timestep)
    n = len(t)
    x = np.zeros(n)

    # Generate OU process
    for i in range(1, n):
        x[i] = x[i-1] + (-x[i-1]/tau)*timestep + sigma*np.sqrt(timestep)*np.random.randn()

    return t, x

# Generate blazar light curve simulations
for i in range(num_simulations):
    # Generate OU process
    t, x = ou_process(tau, sigma, total_time, timestep)

    # Add flares to light curve
    flare_times = np.random.uniform(0, total_time, size=np.random.poisson(5))
    flare_amps = np.random.uniform(0.2, 1.0, size=len(flare_times))
    for j in range(len(flare_times)):
        flare_start = np.argmin(np.abs(t - flare_times[j]))
        flare_end = np.argmin(np.abs(t - (flare_times[j] + np.random.uniform(5, 20))))
        x[flare_start:flare_end] += flare_amps[j]

    # Plot light curve simulation
    plt.figure(figsize=(12, 6))
    plt.plot(t, x, 'k-', linewidth=0.5)
    plt.xlabel('Time (days)')
    plt.ylabel('Flux (Jy)')
    plt.title('Blazar Light Curve Simulation')
    plt.show()
