from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json
import re

load_dotenv()

template = """Create a pet profile with the following information:
For a {animal_type} that is {pet_color} in color.

IMPORTANT: Return ONLY the raw JSON object without any markdown formatting or code blocks.
Do not wrap the response in ```json or ``` tags.

The response should be a plain JSON object with this exact structure:
{{
    "animal_type": "{animal_type}",
    "pet_color": "{pet_color}",
    "superpower": "a unique and funny superpower",
    "pet_name": "a creative name that matches the animal type",
    "css_art": "CSS code that creates additional styling for the pixel art (optional enhancements, not the main structure)"
    - "css_art": must return a complete pixel art block that includes:
      - A <style>...</style> tag with all CSS inside
      - A single container div (e.g. <div class="box">...</div>) containing the 160×160 pixel layout
    - All CSS should be inside the <style> tag — never raw or outside
    - Escape inner quotes with \", and make sure the final result is a single valid JSON object

}}

Make the css_art include any additional styling or effects you want to add to enhance the pixel art representation."""

def generate_pet_name(animal_type, pet_color):
    try:
        llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

        prompt = PromptTemplate(
            template=template,
            input_variables=["animal_type", "pet_color"]
        )

        chain = LLMChain(llm=llm, prompt=prompt)

        # Get the raw response
        response = chain.run({
            "animal_type": animal_type,
            "pet_color": pet_color
        })

        # Clean up the response by removing any markdown code blocks
        cleaned_response = re.sub(r'^```json\s*|\s*```$', '', response.strip())
        cleaned_response = re.sub(r'^```\s*|\s*```$', '', cleaned_response.strip())

        # Try to parse JSON to validate
        try:
            parsed_data = json.loads(cleaned_response)
            return {"pet_data": parsed_data}
        except json.JSONDecodeError:
            # If JSON parsing fails, return a fallback
            return {
                "pet_data": {
                    "animal_type": animal_type,
                    "pet_color": pet_color,
                    "superpower": "the ability to bring joy to everyone they meet",
                    "pet_name": f"Buddy the {animal_type}",
                    "css_art": "/* Additional styling can go here */"
                }
            }

    except Exception as e:
        # Fallback in case of any error
        return {
            "pet_data": {
                "animal_type": animal_type,
                "pet_color": pet_color,
                "superpower": "the ability to bring joy to everyone they meet",
                "pet_name": f"Buddy the {animal_type}",
                "css_art": "/* Additional styling can go here */"
            }
        }
