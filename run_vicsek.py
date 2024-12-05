import numpy as np
import matplotlib.pyplot as plt

def initialize_positions_and_velocities(num_particles, box_size, velocity_magnitude):
    # Initialize positions and velocities
    positions = np.random.rand(num_particles, 2) * box_size
    velocities = np.random.randn(num_particles, 2)
    velocities /= np.linalg.norm(velocities, axis=1)[:, np.newaxis]
    velocities *= velocity_magnitude
    angles = np.arctan2(velocities[:, 1], velocities[:, 0])
    return positions, velocities, angles

def update_positions_and_velocities(positions, velocities, angles, neighborhood_radius, angle_range, velocity_magnitude, box_size):
    # Update positions based on current velocities
    new_positions = (positions + velocities) % box_size
    
    # Update velocities toward average angle of surrounding particles
    num_particles = positions.shape[0]
    for i in range(num_particles):
        displacement = (positions - positions[i]) % box_size
        displacement = np.where(displacement > box_size / 2, displacement - box_size, displacement)
        neighbors = np.where(np.linalg.norm(displacement, axis=1) < neighborhood_radius)[0]
        if len(neighbors) > 0:
            avg_velocity = np.mean(velocities[neighbors], axis=0)
            avg_angle = np.arctan2(avg_velocity[1], avg_velocity[0])
            new_angles = avg_angle + angle_range * (2 * np.random.rand() - 1)
            new_velocities = velocity_magnitude * np.array([np.cos(new_angles), np.sin(new_angles)])
            velocities[i] = new_velocities
    
    return new_positions, velocities, new_angles

def run_simulation(positions, velocities, angles, num_steps, neighborhood_radius, angle_range, velocity_magnitude, box_size):
    # Initialize results
    num_particles = positions.shape[0]
    result_positions = np.zeros((num_steps+1, num_particles, 2))
    result_positions[0] = positions

    result_velocities = np.zeros((num_steps+1, num_particles, 2))
    result_velocities[0] = velocities

    result_angles = np.zeros((num_steps+1, num_particles))
    result_angles[0] = angles

    # Run simulation
    for step in range(num_steps):
        positions, velocities, angles = update_positions_and_velocities(positions, velocities, angles, neighborhood_radius, angle_range, velocity_magnitude, box_size)
        result_positions[step+1] = positions
        result_velocities[step+1] = velocities
        result_angles[step+1] = angles

    return np.array(result_positions), np.array(result_velocities), np.array(result_angles)

def visualize_results(positions, box_size):
    # Plot results
    plt.scatter(positions[:, 0], positions[:, 1])
    plt.xlim(0, box_size)
    plt.ylim(0, box_size)
    plt.show()


def main(num_particles=100, box_size=10, num_steps=100, neighborhood_radius=1, angle_range=0.1, velocity_magnitude=0.1):
    # Run simulation and visualize results
    positions, velocities, angles = initialize_positions_and_velocities(num_particles, box_size, velocity_magnitude)
    positions, velocities, angles = run_simulation(positions, velocities, angles, num_steps, neighborhood_radius, angle_range, velocity_magnitude, box_size)
    for i in range(num_steps):
        visualize_results(positions[i], box_size)
        plt.pause(0.1)
        plt.clf()
    return positions, velocities, angles


