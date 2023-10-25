import streamlit as st

# Title
st.title("Animemore")

# Navigation bar
st.markdown(
    '<div style="background-color: black; padding: 1rem 0;">'
    '<h1 style="color: white; font-weight: 700; letter-spacing: 0.75px; text-align: center;">ANIMORE.to</h1>'
    '</div>',
    unsafe_allow_html=True
)

# Hero section
st.markdown(
    '<div style="min-height: calc(100vh - 5rem); background: rgba(0, 0, 0, 0.6); text-align: center; color: white;">'
    '<h1>Stream Now</h1>'
    '<p>Dive into a world of limitless entertainment at your fingertips. Let\'s start streaming!</p>'
    '<a href="#" style="color: white; border: 1px solid white; text-decoration: none; text-transform: uppercase; padding: 0.75rem 1.5rem;">Explore More</a>'
    '</div>',
    unsafe_allow_html=True
)

# Content divider
st.markdown('<div style="border: 1px solid black; border-radius: 0.25rem; height: 0.5rem; background: linear-gradient(to left, #000, #fff, #000);"></div>', unsafe_allow_html=True)

# Skills section
st.header("Skills")

# Skill 1
st.markdown(
    '<div style="padding: 2.5rem; text-align: center; background: black; transition: all 0.3s linear;">'
    '<i class="fa-solid fa-tv" style="font-size: 2.0rem; margin-bottom: 1.25rem; display: inline-block; color: white;"></i>'
    '<h4 style="color: white;">Stream Now</h4>'
    '<p style="color: #ffffffc2; max-width: 25em; margin: 0 auto;">Stream thousands of Anime sub or dub for Free.</p>'
    '</div>',
    unsafe_allow_html=True
)

# Skill 2
st.markdown(
    '<div style="padding: 2.5rem; text-align: center; background: black; transition: all 0.3s linear;">'
    '<i class="fa-solid fa-book" style="font-size: 2.0rem; margin-bottom: 1.25rem; display: inline-block; color: white;"></i>'
    '<h4 style="color: white;">Read Manga</h4>'
    '<p style="color: #ffffffc2; max-width: 25em; margin: 0 auto;">Dive into captivating manga stories. Read your favorite Manga online.</p>'
    '</div>',
    unsafe_allow_html=True
)

# Contact section
st.header("Contact Us")

st.write("If you have any questions or feedback, please fill out the form below.")

# Contact form
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message", height=5)
submit_button = st.button("Submit")

if submit_button:
    # Process the form data (you can add your logic here)
    st.success("Thank you for your submission!")

st.write("Join us on Discord and be a part of our community: [Discord Link](#)")

# Additional styling for the Discord link
st.markdown('<style>a {color: white; text-decoration: none;} a:hover {color: black;}</style>', unsafe_allow_html=True)
