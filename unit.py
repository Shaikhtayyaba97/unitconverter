import streamlit as st

# Set Page Configuration for better UI
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f7f9fc;
        }
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 18px;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
        .stSelectbox, .stNumberInput {
            font-size: 18px;
        }
        .stTitle {
            font-weight: bold;
            font-size: 28px;
            text-align: center;
        }
        .stMarkdown {
            text-align: center;
            font-size: 20px;
            color: #4A4A4A;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("🔄 Unit Converter App")

# Description
st.markdown("### 🚀 Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category and start converting.")

# User Input - Category Selection
category = st.selectbox(
    "📌 Choose a category",
    ["Length", "Weight", "Time"]
)

# Unit conversion logic
def convert_unit(category, value, unit):
    if category == "Length":
        conversions = {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371
        }
    elif category == "Weight":
        conversions = {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462
        }
    elif category == "Time":
        conversions = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24
        }
    return conversions.get(unit, 0)

# Unit Selection based on Category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours"
    ])

# User Input - Value to Convert
value = st.number_input("🔢 Enter value to convert", min_value=0.0, format="%.2f")

# Convert Button
if st.button("✅ Convert Now"):
    result = convert_unit(category, value, unit)
    st.success(f"🎯 The result is: *{result:.2f}*")