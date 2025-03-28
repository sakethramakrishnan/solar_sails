# visualization.py
import matplotlib.pyplot as plt
from solver import euler_method

def plot_trajectory(x_vals, y_vals):
    """Plots the trajectory of the spacecraft."""
    plt.figure(figsize=(8, 8))
    plt.plot(x_vals, y_vals, label="Spacecraft Trajectory")
    plt.scatter([0], [0], color="yellow", label="Sun")  # Sun at the origin
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.legend()
    plt.title("Solar Sail Spacecraft Trajectory")
    plt.grid()
    plt.show()
