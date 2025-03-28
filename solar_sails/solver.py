# solver.py
import numpy as np
from equations import acceleration
from config import dt, t_max

def euler_method(x0, y0, vx0, vy0):
    """Numerically integrates the equations of motion using Euler's method."""
    num_steps = int(t_max / dt)
    
    # Initialize arrays
    t_vals = np.linspace(0, t_max, num_steps)
    x_vals, y_vals = np.zeros(num_steps), np.zeros(num_steps)
    vx_vals, vy_vals = np.zeros(num_steps), np.zeros(num_steps)

    # Initial conditions
    x_vals[0], y_vals[0] = x0, y0
    vx_vals[0], vy_vals[0] = vx0, vy0

    # Euler integration loop
    for i in range(num_steps - 1):
        ax, ay = acceleration(x_vals[i], y_vals[i], t_vals[i])
        
        vx_vals[i+1] = vx_vals[i] + ax * dt
        vy_vals[i+1] = vy_vals[i] + ay * dt
        x_vals[i+1] = x_vals[i] + vx_vals[i] * dt
        y_vals[i+1] = y_vals[i] + vy_vals[i] * dt
    
    return t_vals, x_vals, y_vals, vx_vals, vy_vals
