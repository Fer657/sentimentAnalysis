import streamlit as st

# Set the background image and linear gradient values
background_image = "pacifistaimagen_K2Cfkcj.width-800.jpg"  # Replace with your image file
gradient_value = "linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6))"

# Create the HTML and CSS for the background
background_html = f"""
<style>
    body {{
        background-image: {gradient_value}, url("{background_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
</style>
"""

# Set the page title and background
st.write(background_html, unsafe_allow_html=True)
st.title("Streamlit Home Page")

# Add content to your home page
st.write("Welcome to my Streamlit homepage!")
