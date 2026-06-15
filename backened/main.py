from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import HTTPException
import traceback

import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Thanmai AI Backend Running"}

from fastapi import HTTPException

@app.post("/chat")
def chat(prompt: Prompt):

    try:
        response = model.generate_content(
            prompt.message
        )

        return {
            "reply": response.text
        }

    except Exception as e:
        error_message = str(e)

        if "quota" in error_message.lower() or "429" in error_message:
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded. Please wait a minute and try again."
            )

        raise HTTPException(
            status_code=500,
            detail=error_message
        )