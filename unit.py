import streamlit as st

# Set Page Configuration for better UI
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS with Background Animation
st.markdown(
    """
    <style>
        /* Background Animation */
        @keyframes gradientAnimation {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .main {
            background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fad0c4, #ffdde1);
            background-size: 400% 400%;
            animation: gradientAnimation 10s ease infinite;
        }

        /* Styling for UI Components */
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 18px;
            transition: transform 0.2s ease-in-out;
        }
        div.stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }

        .stSelectbox, .stNumberInput {
            font-size: 18px;
        }

        .stTitle {
            font-weight: bold;
            font-size: 32px;
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        .stMarkdown {
            text-align: center;
            font-size: 20px;
            color: white;
            font-weight: bold;
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
    conversions = {
        "Length": {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371
        },
        "Weight": {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462
        },
        "Time": {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24
        }
    }
    return conversions.get(category, {}).get(unit, 0)

# Unit Selection based on Category
unit = st.selectbox(
    "🔄 Select Conversion",
    {
        "Length": ["Kilometers to Miles", "Miles to Kilometers"],
        "Weight": ["Kilograms to Pounds", "Pounds to Kilograms"],
        "Time": ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"]
    }[category]
)

# User Input - Value to Convert
value = st.number_input("🔢 Enter value to convert", min_value=0.0, format="%.2f")

# Convert Button
if st.button("✅ Convert Now"):
    result = convert_unit(category, value, unit)
    st.success(f"🎯 The result is: *{result:.2f}*")