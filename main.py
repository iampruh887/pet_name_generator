import langchain_helper as leech
import streamlit as st

st.title("Pets deserve cool names too!")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hen", "Hamster"))

pet_color = st.sidebar.text_area(f"What color is your {animal_type}?", max_chars=15)
