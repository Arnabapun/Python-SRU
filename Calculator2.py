
import streamlit as st
import math

def calculate_isobaric_work(pressure, initial_volume, final_volume):
    delta_v = final_volume - initial_volume
    work = -pressure * delta_v
    return work

def calculate_isothermal_work(n_moles, r_constant, temperature, initial_volume, final_volume):
    if initial_volume == 0 or final_volume == 0:
        raise ZeroDivisionError("Volumes cannot be zero for isothermal process")
    if initial_volume <= 0 or final_volume <= 0:
        raise ValueError("Volumes must be positive for isothermal process")
    work = -n_moles * r_constant * temperature * math.log(final_volume / initial_volume)
    return work

def _streamlit_app():
    st.title("Thermodynamic Work Calculator")

    process_type = st.selectbox(
        "Select Thermodynamic Process:",
        ("Isobaric (Constant Pressure)", "Isothermal (Constant Temperature, Reversible)", "Isochoric (Constant Volume)")
    )

    st.write("-----------")

    work = None

    if process_type == "Isobaric (Constant Pressure)":
        st.header("Isobaric Process (W = -PΔV)")
        pressure = st.number_input("Pressure (P, e.g., Pascals):", value=101325.0, format="%.2f")
        initial_volume = st.number_input("Initial Volume (Vi, e.g., m³):", value=1.0, format="%.2f")
        final_volume = st.number_input("Final Volume (Vf, e.g., m³):", value=2.0, format="%.2f")
        if st.button("Calculate Isobaric Work"):
            work = calculate_isobaric_work(pressure, initial_volume, final_volume)
            st.success(f"Work (W): {work:.2f} Joules")

    elif process_type == "Isothermal (Constant Temperature, Reversible)":
        st.header("Isothermal Process (W = -nRT ln(Vf/Vi))")
        n_moles = st.number_input("Number of Moles (n):", value=1.0, format="%.2f")
        r_constant = st.number_input("Ideal Gas Constant (R, e.g., 8.314 J/(mol·K)):", value=8.314, format="%.3f")
        temperature = st.number_input("Temperature (T, e.g., Kelvin):", value=298.15, format="%.2f")
        initial_volume = st.number_input("Initial Volume (Vi, e.g., m³):", value=1.0, format="%.2f")
        final_volume = st.number_input("Final Volume (Vf, e.g., m³):", value=2.0, format="%.2f")
        if st.button("Calculate Isothermal Work"):
            try:
                work = calculate_isothermal_work(n_moles, r_constant, temperature, initial_volume, final_volume)
                st.success(f"Work (W): {work:.2f} Joules")
            except (ZeroDivisionError, ValueError) as e:
                st.error(f"Calculation Error: {e}")

    elif process_type == "Isochoric (Constant Volume)":
        st.header("Isochoric Process (W = 0)")
        st.info("In an isochoric process (constant volume), no work is done by or on the system.")
        work = 0.0 # Work is zero for isochoric process
        st.success(f"Work (W): {work:.2f} Joules")

    st.write("-----------")
    if work is not None:
        st.write(f"The calculated thermodynamic work is: **{work:.2f} Joules**")

if __name__ == "__main__":
    _streamlit_app()

# Save the content of the Streamlit cell to a Python file
with open('calculator_app.py', 'w') as f:
    f.write(streamlit_app_content)
print("calculator_app.py saved.")
