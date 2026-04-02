from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Parámetros del escenario
numero_dias = 7
numero_ninos = 2
actividad = "playa"

plantilla_prompt = PromptTemplate(
    input_variables=["dias", "numero_ninos", "actividad"],
    template="""
Crea un itinerario de viaje de {dias} días 
para una familia con {numero_ninos} niños, 
que disfrutan de actividades como {actividad}.
"""
)

prompt = plantilla_prompt.format(
    dias=numero_dias,
    numero_ninos=numero_ninos,
    actividad=actividad
)

print("Prompt generado:\n", prompt)

modelo = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    api_key=api_key
)

respuesta = modelo.invoke(prompt)

print("\nRespuesta del modelo:\n")
print(respuesta.content)