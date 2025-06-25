import random
import math
import matplotlib.pyplot as plt
import numpy as np


def buffon_needle_experiment(num_trials, needle_length=1.0, line_spacing=2.0):
    """
    Perform Buffon's needle experiment
    :param num_trials: Number of needle drops
    :param needle_length: Length of the needle (default 1.0)
    :param line_spacing: Distance between parallel lines (default 2.0)
    :return: Estimated value of π
    """
    if needle_length > line_spacing:
        raise ValueError("Needle length must be less than or equal to line spacing")

    crossings = 0  # Count of needle-line intersections

    for _ in range(num_trials):
        # Randomly generate needle position (distance to nearest line)
        y = random.uniform(0, line_spacing / 2)
        # Randomly generate needle angle (0 to π/2)
        theta = random.uniform(0, math.pi / 2)

        # Calculate vertical projection of the needle
        half_projection = (needle_length / 2) * math.sin(theta)

        # Check if needle crosses a line
        if y <= half_projection:
            crossings += 1

    # Calculate π estimate (avoid division by zero)
    if crossings > 0:
        estimated_pi = (2 * needle_length * num_trials) / (crossings * line_spacing)
    else:
        estimated_pi = float('inf')  # Return infinity if no crossings

    return estimated_pi


def analyze_precision(max_trials=100000, step=1000):
    """
    Analyze the effect of trial count on estimation precision
    :param max_trials: Maximum number of trials
    :param step: Step size for recording results
    """
    # Store results
    trial_counts = []
    pi_estimates = []
    errors = []

    # Perform experiments with increasing trial counts
    for n in range(step, max_trials + 1, step):
        pi_est = buffon_needle_experiment(n)
        trial_counts.append(n)
        pi_estimates.append(pi_est)
        errors.append(abs(pi_est - math.pi))

    # Create plots
    plt.figure(figsize=(14, 10))

    # Plot 1: π estimates over trials
    plt.subplot(2, 2, 1)
    plt.plot(trial_counts, pi_estimates, 'b-', alpha=0.7)
    plt.axhline(y=math.pi, color='r', linestyle='--')
    plt.xlabel('Number of Trials')
    plt.ylabel('π Estimate')
    plt.title('π Estimate vs. Number of Trials')
    plt.grid(True)

    # Plot 2: Absolute error over trials
    plt.subplot(2, 2, 2)
    plt.plot(trial_counts, errors, 'r-')
    plt.xlabel('Number of Trials')
    plt.ylabel('Absolute Error')
    plt.title('Absolute Error vs. Number of Trials')
    plt.grid(True)

    # Plot 3: Error in log-log scale
    plt.subplot(2, 2, 3)
    plt.loglog(trial_counts, errors, 'g-')
    plt.xlabel('Number of Trials (log scale)')
    plt.ylabel('Absolute Error (log scale)')
    plt.title('Error vs. Trials (Log-Log Scale)')
    plt.grid(True)

    # Plot 4: Distribution of π estimates
    plt.subplot(2, 2, 4)
    plt.hist(pi_estimates, bins=30, alpha=0.7, color='purple')
    plt.axvline(x=math.pi, color='r', linestyle='--', linewidth=2)
    plt.xlabel('π Estimate')
    plt.ylabel('Frequency')
    plt.title('Distribution of π Estimates')

    plt.tight_layout()
    plt.show()

    # Print final results
    final_estimate = pi_estimates[-1]
    final_error = errors[-1]
    print(f"Final result (Trials={max_trials}):")
    print(f"Estimated π = {final_estimate:.6f}")
    print(f"Actual π    = {math.pi:.6f}")
    print(f"Absolute error = {final_error:.6f}")
    print(f"Relative error = {abs(final_error / math.pi) * 100:.4f}%")


# Main program
if __name__ == "__main__":
    # Set experiment parameters
    TRIALS = 100000  # Total number of trials

    # Perform a full experiment
    estimated_pi = buffon_needle_experiment(TRIALS)
    print(f"After {TRIALS} needle drops, estimated π = {estimated_pi:.6f}")
    print(f"Actual π value: {math.pi:.6f}")
    print(f"Absolute error: {abs(estimated_pi - math.pi):.6f}")

    # Analyze effect of trial count on precision
    print("\nAnalyzing the effect of trial count on estimation precision...")
    analyze_precision(max_trials=100000, step=1000)
