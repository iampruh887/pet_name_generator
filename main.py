import langchain_helper as leech
import streamlit as st
import streamlit.components.v1 as components
import json
from bs4 import BeautifulSoup

st.set_page_config(page_title="Pet Name Generator", layout="centered")
st.title("🐾 Make your pet more interesting 👍")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hen", "Hamster"))
pet_color = st.sidebar.text_area(f"What color is your {animal_type}?", max_chars=15)

# Use the color input or default to a generic color
color_to_use = pet_color if pet_color else "brown"

# Get the response
response = leech.generate_pet_name(animal_type, color_to_use)

try:
    # Extract the pet data
    pet_data = response['pet_data']

    # Extract individual fields
    pet_name = pet_data['pet_name']
    superpower = pet_data['superpower']
    css_art = pet_data.get('css_art', '')
    animal = pet_data['animal_type']
    color = pet_data['pet_color']

    # Separate <style> and HTML from css_art
    soup = BeautifulSoup(css_art, "html.parser")
    style_tag = soup.find("style")
    style_block = str(style_tag) if style_tag else ""
    if style_tag:
        style_tag.decompose()  # remove <style> tag from the soup so only HTML remains
    pixel_art_markup = str(soup)

    # Final HTML wrapped in iframe-safe page
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    {style_block}
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Segoe UI', sans-serif;
            color: white;
            text-align: center;
        }}
        .card {{
            background-color: #fff;
            color: #222;
            padding: 30px;
            border-radius: 20px;
            width: 320px;
            margin: 40px auto;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        .details p {{ margin: 8px 0; }}
    </style>
    </head>
    <body>
        <div class="card">
            <h2>Meet <strong>{pet_name}</strong> 🐾</h2>
            <div class="details">
                <p><strong>Type:</strong> {animal}</p>
                <p><strong>Color:</strong> {color}</p>
                <p><strong>Superpower:</strong> {superpower}</p>
            </div>
            <div style="margin-top: 20px;">
                {pixel_art_markup}
            </div>
        </div>
    </body>
    </html>
    """

    components.html(full_html, height=450)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.write("Response received:", response)

    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(f"## 🐾 {animal_type} Profile")
        st.markdown(f"**Color:** {color_to_use}")
        st.markdown(f"**Name:** Buddy the {animal_type}")
        st.markdown(f"**Superpower:** Bringing joy to everyone!")

        emoji_map = {
            'Cat': '🐱',
            'Dog': '🐶',
            'Cow': '🐄',
            'Hen': '🐔',
            'Hamster': '🐹'
        }

        st.markdown(f"<div style='text-align: center; font-size: 60px; margin: 20px 0;'>" + emoji_map.get(animal_type, '🐾') + "</div>", unsafe_allow_html=True)
