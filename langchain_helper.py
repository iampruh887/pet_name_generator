from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()



# display_rules = "You are a Dog name suggesting agent. Be as creative as you can with how you are going to display the names on the command line interface. Dont just use markdown to display the names be inhumanely and insanely creative in the way you show the names, for example you can use (+_+) ASCII art. Also if you are going to use ASCII art, never use the same ASCII art for every name, also the ASCII art need not necessarily be a dog."

display_rules = "Give the output in a json format 'animal_type': animal_type, 'pet_color':pet_color , 'superpower': a random unhinged superpower, 'pet_name': the actual pet name, 'css_art': css script for the art"

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
