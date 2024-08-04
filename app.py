import streamlit as st
import math

def calculate_vdot(dist, t):
    speed = dist / (t * 60)  # Convert minutes to seconds
    numerator = -4.6 + 0.182258 * speed + 0.000104 * speed**2
    denominator = 0.8 + 0.1894393 * math.exp(-0.012778 * t * 60) + 0.2989558 * math.exp(-0.1932605 * t * 60)
    vdot = numerator / denominator
    return vdot

def time_to_minutes(hhmmss):
    hh, mm, ss = map(int, hhmmss.split(':'))
    total_minutes = hh * 60 + mm + ss / 60
    return total_minutes

def main():
    st.title("Race Vdot Calculator")

    st.subheader("Select your race distance and enter your time")

    race_options = {
        "1500m": 1500,
        "1 milla": 1609.34,
        "3000m": 3000,
        "5km": 5000,
        "10km": 10000,
        "15km": 15000,
        "medio maratón (21k)": 21097.5,
        "maratón (42k)": 42195
    }

    race_distance = st.selectbox("Select Race Distance", list(race_options.keys()))
    time = st.text_input("Enter Time (hh:mm:ss)")

    if st.button("Calculate Vdot"):
        dist = race_options[race_distance]
        t = time_to_minutes(time)
        vdot = calculate_vdot(dist, t)
        st.write(f"Your Vdot is: {vdot:.2f}")

if __name__ == "__main__":
    main()
