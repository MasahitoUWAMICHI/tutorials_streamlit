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

st.sidebar.header("Run Simulation")

run_simulation = st.sidebar.toggle("Run simulation", False)

if run_simulation:
    if 'simulation_results' not in st.session_state:
        positions, velocities = run_vicsek.initialize_positions_and_velocities(num_particles, box_size, velocity_magnitude)
        result_positions, result_velocities = run_vicsek.run_simulation(positions, velocities, num_steps, neighborhood_radius, angle_range, velocity_magnitude, box_size)
        st.session_state.simulation_results = (result_positions, result_velocities)
    else:
        result_positions, result_velocities = st.session_state.simulation_results

    st.header("Simulation Results")

    step_to_display = st.slider("Step to display", 0, num_steps, 0)

    fig, ax = run_vicsek.visualize_results(result_positions[step_to_display], result_velocities[step_to_display], box_size)
    st.pyplot(fig)
else:
    if 'simulation_results' in st.session_state:
        del st.session_state.simulation_results