# main.py
from solver import euler_method
from visualization import plot_trajectory
from config import r0

if __name__ == "__main__":
    # Initial conditions: starting at 1 AU, moving tangentially with Earth's orbital velocity
    x0, y0 = r0, 0
    vx0, vy0 = 0, 29780  # Earth's orbital speed in m/s

    # Run simulation
    t_vals, x_vals, y_vals, vx_vals, vy_vals = euler_method(x0, y0, vx0, vy0)

    # Plot results
    plot_trajectory(x_vals, y_vals)
