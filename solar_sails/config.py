# config.py

# Physical Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
M_sun = 1.989e30  # Mass of the Sun (kg)
P0 = 4.57e-6  # Solar radiation pressure at 1 AU (N/m^2)
r0 = 1.496e11  # 1 AU in meters
epsilon = 0.1  # Amplitude of solar pressure fluctuation
omega = 2 * 3.14159 / (27 * 24 * 3600)  # Approximate solar activity frequency (27-day cycle)
phi = 0  # Phase shift

# Spacecraft properties
sail_area = 100  # m^2 (sail area)
mass = 100  # kg (mass of the spacecraft)

# Simulation parameters
dt = 60  # Time step in seconds (1 minute)
t_max = 3.154e7  # Total simulation time (1 year in seconds)
