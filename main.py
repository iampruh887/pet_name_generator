import langchain_helper as leech
import streamlit as st
import json

st.set_page_config(page_title="Pet Name Generator", layout="centered")
st.title("🐾 Pets Deserve Cool Names Too!")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hen", "Hamster"))
pet_color = st.sidebar.text_area(f"What color is your {animal_type}?", max_chars=15)

if pet_color:
    response = leech.generate_pet_name(animal_type, pet_color)
else:
    response = leech.generate_pet_name(animal_type, "irrelevant")

# Parse JSON string returned under 'pet_name'
pet_data = json.loads(response['pet_name'])

# Extract individual fields
pet_name = pet_data['pet_name']
superpower = pet_data['superpower']
css_art = pet_data['css_art']
animal = pet_data['animal_type']
color = pet_data['pet_color']

# --- Display the card with HTML & CSS ---
html_code = f"""
<style>
.card {{
    background-color: #f8f9fa;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    width: 400px;
    margin: 40px auto;
    font-family: 'Segoe UI', sans-serif;
    text-align: center;
    position: relative;
}}
.card h2 {{
    margin: 10px 0;
    color: #333;
}}
.card p {{
    color: #555;
}}
.box-wrapper {{
    position: relative;
    height: 200px;
    margin-top: 30px;
}}
{css_art}
</style>

<div class="card">
    <h2>Meet <strong>{pet_name}</strong> 🐾</h2>
    <p><strong>Type:</strong> {animal}</p>
    <p><strong>Color:</strong> {color}</p>
    <p><strong>Superpower:</strong><br>{superpower}</p>
    <div class="box-wrapper">
        <div class="box"></div>
        <div class="cat in-box"></div>
    </div>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
