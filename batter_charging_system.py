import streamlit as st

# Define battery types and their parameters
BATTERY_TYPES = {
    "Li-ion": {"capacity": 3000, "color": "green"},
    "Li-Po": {"capacity": 2500, "color": "blue"},
    "NiMH": {"capacity": 1800, "color": "purple"},
    "Lead-Acid": {"capacity": 7000, "color": "orange"}
}

st.set_page_config(page_title="Battery Charge Simulator ⚡", page_icon="🔋")

st.title("🔋 Battery Charging & Discharging UI")
st.markdown("Select a battery type and simulate charge/discharge cycles.")

# Battery selection
battery_type = st.selectbox("Choose Battery Type", list(BATTERY_TYPES.keys()))

# Initialize charge level
if "level" not in st.session_state:
    st.session_state.level = 50  # start at 50%

color = BATTERY_TYPES[battery_type]["color"]

# Show progress bar & battery info
st.subheader(f"Selected: {battery_type}")
st.progress(st.session_state.level)
st.write(f"**Battery Level:** {st.session_state.level}%")
st.write(f"**Capacity:** {BATTERY_TYPES[battery_type]['capacity']} mAh")

# Charge / Discharge controls
col1, col2 = st.columns(2)
if col1.button("🔌 Charge"):
    st.session_state.level = min(st.session_state.level + 10, 100)
if col2.button("⚡ Discharge"):
    st.session_state.level = max(st.session_state.level - 10, 0)

# Add a little style tip for more advanced design (optional)
st.markdown(
    """
    <style>
    .stProgress > div > div > div > div {
        background-color: %s;
    }
    </style>
    """ % color, unsafe_allow_html=True
)

# Battery info table
st.markdown("### Battery Types Overview")
st.table({
    "Type": list(BATTERY_TYPES.keys()),
    "Main Features": [
        "High energy density, long life, light weight",
        "Lighter, flexible shapes, high C-rate",
        "Moderate energy, safe, environmentally friendly",
        "Cheap, heavy, high surge current"
    ],
    "Typical Uses": [
        "Phones, laptops",
        "Drones, RC devices",
        "AA/AAA cells, hybrid cars",
        "Automobiles, UPS"
    ]
})
