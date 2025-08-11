import random
import math
import matplotlib.pyplot as plt

def monte_carlo_pi_realtime(num_points=10000, update_interval=100):
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []
    inside_circle = 0
    estimates = []
    steps = []

    plt.ion()  # Turn on interactive mode
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6,10))

    for i in range(1, num_points + 1):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) <= 1:
            inside_circle += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)

        # Update every few points
        if i % update_interval == 0 or i == num_points:
            pi_estimate = (inside_circle / i) * 4
            estimates.append(pi_estimate)
            steps.append(i)

            # --- Scatter plot ---
            ax1.clear()
            ax1.scatter(inside_x, inside_y, color='blue', s=1, label="Inside quarter circle")
            ax1.scatter(outside_x, outside_y, color='red', s=1, label="Outside quarter circle")
            ax1.set_aspect('equal', adjustable='box')
            ax1.set_xlabel('x')
            ax1.set_ylabel('y')
            ax1.set_title(f'Points Thrown: {i}  |  π Estimate: {pi_estimate:.5f}')
            ax1.legend()

            # --- Convergence plot ---
            ax2.clear()
            ax2.plot(steps, estimates, label="Estimated π", color="blue")
            ax2.axhline(math.pi, color="red", linestyle="--", label="Actual π")
            ax2.set_xlabel("Number of Points")
            ax2.set_ylabel("Estimated π Value")
            ax2.set_title("Convergence of Monte Carlo π")
            ax2.legend()
            ax2.grid(True)

            plt.pause(0.001)  # Brief pause for animation

    plt.ioff()
    plt.show()

# Run simulation
monte_carlo_pi_realtime(50000, update_interval=50)
