import run_vicsek
import streamlit as st

st.title("Vicsek Model Simulation")

st.sidebar.header("Simulation Parameters")

num_particles = st.sidebar.slider("Number of particles", 10, 100, 50)

box_size = st.sidebar.slider("Box size", 5.0, 20.0, 10.0)

num_steps = st.sidebar.slider("Number of steps", 10, 200, 100)

neighborhood_radius = st.sidebar.slider("Neighborhood radius", 0.1, 2.0, 1.0)

angle_range = st.sidebar.slider("Angle range", 0.01, 0.5, 0.1)

velocity_magnitude = st.sidebar.slider("Velocity magnitude", 0.01, 0.5, 0.1)

positions, velocities, angles = run_vicsek.initialize_positions_and_velocities(num_particles, box_size, velocity_magnitude)
