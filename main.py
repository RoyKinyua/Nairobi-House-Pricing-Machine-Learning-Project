import streamlit as st
import pandas as pd
import numpy as np
import joblib


st.set_page_config(page_title="Nairobi Property Price Predictor",
                   layout="wide")

st.title("🏠 Nairobi Property Price Predictor")
st.write("Estimate property prices using machine learning.")


model = joblib.load("models/model.pkl")

# Optional: Hardcode MAE from Day 3
MODEL_MAE = 4639232.1873 

st.sidebar.header("Property Details")

location = st.sidebar.selectbox(
    "Location",
    ["westlands", "kilimani", "kileleshwa",
     "lavington", "parklands", "karen",
     "runda", "south b", "south c"]
)

bedrooms = st.sidebar.slider("Bedrooms", 1, 6, 3)
bathrooms = st.sidebar.slider("Bathrooms", 1, 5, 2)
size_sqft = st.sidebar.number_input("Size (sqft)", 300, 10000, 1200)

amenities = st.sidebar.multiselect(
    "Amenities",
    ["parking", "gym", "swimming pool",
     "lift", "security", "garden"]
)

listing_month = st.sidebar.selectbox("Listing Month", list(range(1, 13)))

# ---------------------------------------------------
# Feature Engineering
# ---------------------------------------------------

amenity_score = len(amenities)

distance_map = {
    "westlands": 3,
    "kilimani": 5,
    "kileleshwa": 4,
    "lavington": 6,
    "parklands": 4,
    "karen": 15,
    "runda": 12,
    "south b": 8,
    "south c": 7
}

distance_to_cbd_km = distance_map[location]

input_dict = {
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "size_sqft": size_sqft,
    "amenity_score": amenity_score,
    "distance_to_cbd_km": distance_to_cbd_km,
    "month": listing_month
}

input_df = pd.DataFrame([input_dict])


for loc in distance_map.keys():
    if loc != "westlands":  # if you used drop_first=True
        input_df[f"location_{loc}"] = 1 if location == loc else 0


if st.button("Predict Price"):

    prediction = model.predict(input_df)[0]

    lower_bound = prediction - MODEL_MAE
    upper_bound = prediction + MODEL_MAE

    st.subheader("💰 Predicted Price")
    st.success(f"KES {prediction:,.0f}")

    st.write(
        f"Estimated range: KES {lower_bound:,.0f} – KES {upper_bound:,.0f}"
    )



    st.subheader("📊 Key Price Drivers")

    explanation = []

    if size_sqft > 2000:
        explanation.append("Large property size increases value.")
    if location in ["karen", "runda", "lavington"]:
        explanation.append("Premium location significantly boosts price.")
    if amenity_score >= 4:
        explanation.append("High amenity count adds strong value.")
    if distance_to_cbd_km > 10:
        explanation.append("Distance from CBD slightly reduces price.")

    for item in explanation:
        st.write("•", item)


st.markdown("---")
st.caption("Built by Roy Kinyua | Nairobi Property ML Project")

