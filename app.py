import streamlit as st
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="Smart Sprinkler System", page_icon="💧", layout="wide")

# Load the model
model = joblib.load("Farm_Irrigation_System.pkl")

# App title
st.title("💧 Smart Sprinkler Control Panel")
st.markdown(
    """
    Welcome to the **Smart Sprinkler System**   
    Enter the **scaled sensor values** (between 0 and 1) from your field, and the system will predict which **sprinklers should be ON** to optimize irrigation.  
    """
)

st.subheader("📊 Input Sensor Values (0 to 1)")

sensor_values = []
columns = st.columns(4)

for i in range(20):
    with columns[i % 4]:
        val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        sensor_values.append(val)

st.markdown("---")
if st.button("🚀 Predict Sprinkler Status"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.success("✅ Prediction completed!")
    st.markdown("### 💡 Sprinkler Status:")

    status_table = []
    for i, status in enumerate(prediction):
        status_table.append({
            "Parcel": f"Parcel {i}",
            "Sprinkler Status": "🟢 ON" if status == 1 else "🔴 OFF"
        })

    st.table(status_table)

st.markdown("---")
st.markdown(
    "<div style='text-align:center;'>"
    "Made for Edunet Internship | Powered by Streamlit & Machine Learning"
    "</div>",
    unsafe_allow_html=True,
)
