import streamlit as st
import pandas as pd
import pickle
from datetime import date

# ---------------- Load Model ----------------
model = pickle.load(open(r"D:\Studys\GUVI\GUVI Project\Content Monetization Modeler\Content Monetization Modeler_python_code\.venv\code\pipe_xgb .pkl", "rb"))


st.set_page_config(page_title="YouTube Revenue Prediction", layout="centered")

st.title("📺 YouTube Revenue Prediction Dashboard")
st.sidebar.header("📌 Input Video Details")

# ---------------- User Inputs ----------------
views = st.sidebar.number_input("Views", min_value=0, step=1, format="%d")
likes = st.sidebar.number_input("Likes", min_value=0, step=1, format="%d")
comments = st.sidebar.number_input("Comments", min_value=0, step=1, format="%d")
watch_time_minutes = st.sidebar.number_input("Watch Time (minutes)", min_value=0.0, step=10.0, format="%.1f")
subscribers = st.sidebar.number_input("Subscribers", min_value=0, step=1, format="%d")

upload_date = st.sidebar.date_input("Video Upload Date", min_value=date(2005,1,1), max_value=date.today())

category = st.sidebar.selectbox("Category", ["Education","Music","Tech","Entertainment","Gaming","Lifestyle"])
device = st.sidebar.selectbox("Device", ["TV","Mobile","Desktop","Tablet"])
country = st.sidebar.selectbox("Country", ["CA","DE","IN","AU","UK","US"])

# ---------------- Feature Engineering ----------------
engagement_rate = (likes + comments) / views if views > 0 else 0

year = upload_date.year
month = upload_date.month
dayofweek = upload_date.weekday()

# ---------------- Input DataFrame (MUST match training features) ----------------
input_data = pd.DataFrame({
    "views": [views],
    "likes": [likes],
    "comments": [comments],
    "subscribers": [subscribers],
    "engagement_rate": [engagement_rate],
    "watch_time_minutes": [watch_time_minutes],
    "year": [year],
    "month": [month],
    "dayofweek": [dayofweek],
    "category": [category],
    "device": [device],
    "country": [country]
})
# -----------------------------
# Display Input Summary
# -----------------------------
col1, col2 = st.columns(2)
with col1:
    st.write(f"**Views**: {views}")
    st.write(f"**Likes**: {likes}")
    st.write(f"**Comments**: {comments}")
    st.write(f"**Watch Time**: {watch_time_minutes:.1f} min")
    st.write(f"**Subscribers**: {subscribers}")
with col2:
    st.write(f"**Upload Date**: {upload_date.strftime('%Y-%m-%d')}")
    st.write(f"**Category**: {category}")
    st.write(f"**Device**: {device}")
    st.write(f"**Country**: {country}")
    

# ---------------- Prediction ----------------
if st.sidebar.button("🎯 Predict Revenue"):

    # Rule: If no views → predict 0
    if views == 0:
        st.success("💰 Predicted Revenue: **$0.00 USD**")
    else:
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Predicted Revenue: **${prediction:.2f} USD**")


# -----------------------------
# Set Custom Background Color #0e1117
# -----------------------------
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117; /* Dark blue-black */
        color: white;
    }
    .stApp {
        background-color: #E8B298;
    }
    .css-1d391kg {
        background-color: #0e1117;
    }
    .css-1cpxqw2 {
        color: gold;
    }
    .stButton>button {
        background-color: #3fe625;
        color: white;
        border-radius: 12px;
        font-size: 16px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Run with: streamlit run app.py