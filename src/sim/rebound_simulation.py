"""
IX-Darkstar Simulation – rebound_simulation.py

Simulates a simplified 1D oscillating core between two magnetic caps inside a vacuum chamber.
Models rebound velocity, induction damping, asymmetry bias, and net drift over time.

Author: Bryce W.
Version: 0.1
"""

import matplotlib.pyplot as plt

# --- Simulation Parameters ---
mass = 0.35                # kg (mass of core)
initial_velocity = 2.0     # m/s (initial pulse)
damping_factor = 0.998     # 1 = no loss, <1 = energy loss per impact
bias = 0.0012              # directional energy bias per rebound (adds net drift)
cycles = 2000              # number of bounces to simulate
distance = 0.0             # starting displacement

# --- Lists to Track ---
positions = [0]
velocities = [initial_velocity]
times = [0]

# --- Main Simulation Loop ---
for i in range(1, cycles + 1):
    direction = -1 if i % 2 == 0 else 1  # left or right rebound
    prev_v = velocities[-1]

    # Apply energy loss on impact
    v_after = abs(prev_v) * damping_factor

    # Inject directional bias to simulate asymmetric gating or coil loading
    v_after += direction * bias

    # Update velocity and displacement
    velocities.append(v_after * direction)
    distance += v_after * direction * 0.05  # dt of 0.05s per cycle
    times.append(times[-1] + 0.05)
    positions.append(distance)

# --- Final Output ---
print(f"Final net drift after {cycles} cycles: {distance:.4f} meters")

# --- Visualization ---
plt.figure(figsize=(10, 4))
plt.plot(times, positions, label="Core Position (m)", color="cyan")
plt.title("IX-Darkstar Oscillating Core Drift Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
