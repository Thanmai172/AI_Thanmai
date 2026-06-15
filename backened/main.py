from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# -----------------------------
# Provider Selection
# -----------------------------
provider = os.getenv("AI_PROVIDER", "groq").lower()

# -----------------------------
# Gemini Setup
# -----------------------------
if provider == "gemini":
    import google.generativeai as genai

    genai.configure(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    gemini_model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

# -----------------------------
# Groq Setup
# -----------------------------
elif provider == "groq":
    from groq import Groq

    groq_client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

# -----------------------------
# FastAPI App
# -----------------------------
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

# -----------------------------
# Request Model
# -----------------------------
class Prompt(BaseModel):
    message: str

# -----------------------------
# Home Route
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Thanmai AI Backend Running",
        "provider": provider
    }

# -----------------------------
# Chat Route
# -----------------------------
@app.post("/chat")
def chat(prompt: Prompt):

    try:

        # ---------------------
        # Gemini
        # ---------------------
        if provider == "gemini":

            response = gemini_model.generate_content(
                prompt.message
            )

            return {
                "provider": "Gemini",
                "reply": response.text
            }

        # ---------------------
        # Groq
        # ---------------------
        elif provider == "groq":

            response = groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt.message
                    }
                ],
                model="llama-3.3-70b-versatile"
            )

            return {
                "provider": "Groq",
                "reply": response.choices[0].message.content
            }

        else:
            raise HTTPException(
                status_code=400,
                detail="Invalid AI_PROVIDER in .env"
            )

    except Exception as e:

        error_message = str(e)

        if "quota" in error_message.lower() or "429" in error_message:
            raise HTTPException(
                status_code=429,
                detail="API quota exceeded. Please try again later."
            )

        raise HTTPException(
            status_code=500,
            detail=error_message
        )