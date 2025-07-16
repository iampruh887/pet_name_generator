from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()



display_rules = """
Return the output as a valid JSON object with the following keys:

- "animal_type": the type of animal (e.g., "Cat", "Hamster")
- "pet_color": the pet's color (e.g., "yellow-green", "sky blue")
- "superpower": a wildly overpowered but hilariously useless ability — it should be cute, absurd, and clearly impractical for humans or AI
- "pet_name": a unique, creative, and fun name
- "css_art": a pixel-style CSS artwork representing the pet

Instructions for "css_art":
- The artwork must use a fixed container element (e.g., <div class="box">...</div>)
- The container should be exactly 160px × 160px and must contain various colours to simulate the response
- All positioning and layout must be relative to the `.box` — avoid absolute positioning outside it
- Each pixel should be uniquely colored (avoid leaving any white)
- Make the layout loosely resemble the given animal
- Escape all quotes in HTML and CSS properly using `\"`
- Avoid unescaped newlines

Important:
- Only return the JSON object — no markdown formatting (e.g., no ```json)
- The entire response must be valid JSON
"""


prompt= "I have a {animal_type} pet which is {pet_color} in colour and I want a cool name for it. Suggest me one cool name for my pet."

push4art = "based on the superpower and animal_type, you must generate a css art code that defines the description of the pet perfectly. The CSS is allowed to contain ASCII art embedded within it to depict the exact type of animal that we are discussig about. Return a plain JSON object without any markdown formatting or extra escaping. No ```json, no backslashes."

def generate_pet_name(animal_type, pet_color):
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template= display_rules + prompt + push4art
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response

if __name__ == "__main__":
    print(generate_pet_name("cow", "golden"))
