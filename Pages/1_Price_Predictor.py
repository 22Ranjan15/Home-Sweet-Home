import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Price Predictor")

with open('Datasets/df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.header("Enter Your Inputs: \n Note: This model doesn't work with creazy data. Please enter valid data.")

# Property Type Dropdown Menu
property_type = st.selectbox("Property Type", ['flat', 'house'])

# Sector
sector = st.selectbox("Sector", sorted(df['sector'].unique().tolist()))

# Bed Rooms
bedrooms = float(st.selectbox("Number of Bedroom", sorted(df['bedRoom'].unique().tolist())))

# Bath Rooms
bathrooms = float(st.selectbox("Number of Bathroom", sorted(df['bathroom'].unique().tolist())))

# Balcony
balcony = st.selectbox("Balconies", sorted(df['balcony'].unique().tolist()))

# AgePossession[Age of Property]
agePossession = st.selectbox("Property age", sorted(df['agePossession'].unique().tolist()))

# Built Up Area
built_up_area = float(st.number_input("Built Up Area"))

# Servent Room
servant_room = float(st.selectbox("Servent Room", [0.0, 1.0]))

# Store room 
store_room = float(st.selectbox("Store Room", [0.0, 1.0]))

# Furnishing Type
furnish_type = st.selectbox("Furnishing Type", sorted(df['furnishing_type'].unique().tolist()))

# Luxury Category 
luxury_category = st.selectbox("Luxury Category", sorted(df['luxury_category'].unique().tolist()))  

# Floor Category
floor_category = st.selectbox("Floor Category", sorted(df['floor_category'].unique().tolist()))

if st.button('Predict Price'):
    # form a dataframe
    data = [[property_type, sector, bedrooms, bathrooms, balcony, agePossession, built_up_area, servant_room, store_room, furnish_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)
    one_df

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display the result
    st.text(f"The price of the property is between {np.round(low, 2)} Cr and {np.round(high, 2)} Cr")
