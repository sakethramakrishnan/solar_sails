# equations.py
import numpy as np
from config import G, M_sun, P0, r0, epsilon, omega, phi, sail_area, mass

def acceleration(x, y, t):
    """Computes acceleration due to gravity and radiation pressure."""
    r = np.sqrt(x**2 + y**2)
    
    # Gravitational acceleration
    a_grav_x = -G * M_sun * x / r**3
    a_grav_y = -G * M_sun * y / r**3
    
    # Fluctuating radiation pressure
    P = P0 * (r0 / r)**2 * (1 + epsilon * np.sin(omega * t + phi))
    a_rad_x = (P * sail_area / mass) * (x / r)
    a_rad_y = (P * sail_area / mass) * (y / r)

    return a_grav_x + a_rad_x, a_grav_y + a_rad_y
