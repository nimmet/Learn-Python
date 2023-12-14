
import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    image = st.camera_input("Camera")

if image:
    img = Image.open(image)
    gray_img = img.convert("L")
    st.image(gray_img)