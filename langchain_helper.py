from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()



display_rules = "You are a Dog name suggesting agent. Be as creative as you can with how you are going to display the names on the command line interface. Dont just use markdown to display the names be inhumanely and insanely creative in the way you show the names, for example you can use (+_+) ASCII art. Also if you are going to use ASCII art, never use the same ASCII art for every name, also the ASCII art need not necessarily be a dog."

prompt="I have a pet dog and I need a cool name for it. Suggest me a cool name for my pet."
prompt = display_rules + prompt
def generate_pet_name(animal_type, pet_color):
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=1)
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template= display_rules + "I have a {animal_type} pet which is {pet_color} in colour and I want a cool name for it. Suggest me one cool name for my pet."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response

if __name__ == "__main__":
    print(generate_pet_name("cow", "golden"))
