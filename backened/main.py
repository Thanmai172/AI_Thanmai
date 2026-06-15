from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

class Prompt(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Thanmai AI Backend Running"}

@app.post("/chat")
def chat(prompt: Prompt):

    response = model.generate_content(
        prompt.message
    )

    return {
        "reply": response.text
    }