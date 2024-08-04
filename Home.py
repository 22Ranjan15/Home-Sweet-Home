import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Home Sweet Home",
    page_icon="🏠",
)

# Side Bar -- Developer's Details
st.sidebar.header("Developer:")
name = "Ranjan Das"
email = "ranjan221523@gmail.com"
linkedin = "https://www.linkedin.com/in/ranjan-das-62a331290/"

st.sidebar.write(f"**Name:** {name}.")
st.sidebar.write(f"**Email:** {email}")
st.sidebar.write(f"**LinkedIn:** [{name}]({linkedin})")



# Title of the page
st.title("Welcome to Home Sweet Home")

# Main header
st.header("Your Ultimate Real Estate Companion")

# Introduction 
st.write("""
At Home Sweet Home, we’re here to make your real estate journey smooth, informed, and delightful. Whether you're buying, selling, or simply exploring, our platform offers the insights you need, tailored just for you.
""")

# Navigation Section Title
st.subheader("Navigation")

# Price Predictor Section
# st.header("Price Predictor")
# st.write("")

# What We Offer section
# st.subheader("What We Offer")

st.write("**Personalized Price Predictions**")
st.write("""
Curious about the value of a home? Our state-of-the-art algorithms provide price predictions based on your unique preferences. Just share the property details, and we’ll deliver a spot-on valuation, customized to your needs.
""")

st.write("**Comprehensive Area Analysis**")
st.write("""
Dreaming of the perfect neighborhood? Our platform lets you analyze any area based on your inputs, offering detailed insights into market trends and local amenities. Discover the best places to live, invest, or simply enjoy.
""")

st.write("**Similar Property Suggestions**")
st.write("""
Want more options? Home Sweet Home doesn’t stop at price predictions. We also suggest similar properties that match your preferences, expanding your choices and making your search effortless.
""")

# How It Works section
st.subheader("How It Works")

st.write("""
1. **Enter Property Details**: Provide the key details of the property, such as location, size, and special features.
2. **Analyze & Predict**: Our cutting-edge technology analyzes your input and gives you an accurate price prediction and area analysis.
3. **Explore Similar Properties**: Discover similar homes that fit your criteria, giving you more options to choose from.
""")

# Why Choose Home Sweet Home section
st.subheader("Why Choose Home Sweet Home?")

st.write("""
- **Accurate & Reliable**: Get the most precise and up-to-date information with our data-driven approach.
- **User-Friendly**: Enjoy a seamless experience with our intuitive platform designed just for you.
- **Comprehensive Insights**: From price predictions to area analysis and property suggestions, we’ve got you covered.
""")

# Call to Action section
st.subheader("Start Your Journey Today")

st.write("""
Join the Home Sweet Home community and take the guesswork out of real estate. Whether you're a buyer, seller, or just exploring, we’re here to help you make smarter, more confident decisions.
""")

st.write("**Discover your dream home with Home Sweet Home – where your perfect property is just a few clicks away.**")

# Query Section
st.subheader("Query")
st.write("Have a question or need assistance? Feel free to reach out to us.")
# Input fields for submitting a review
with st.form(key='query_form'):
    name = st.text_input("Your Name")
    query = st.text_area("Your Query")
    submit_button = st.form_submit_button("Submit Query")

    if submit_button:
        if name and query:
            # Display the query
            st.write(f"**{name}** says:")
            st.write(query)
            st.success("Thank you for your query!")
        else:
            st.error("Please enter both your name and your query.")




# Footer Section
st.markdown("---")  # A horizontal line to separate the footer

st.markdown("""
    **Contact Us**
    - Phone: 8918763394
    - Email: msd23012@iiitl.ac.in
    - Address: IIIT Lucknow, Chak Ganjaria, C.G. City, Lucknow-226002, Uttar Pradesh, India
            
    **Copyright**
    - © 2024 Home Sweet Home. All rights reserved.
""", unsafe_allow_html=True)
