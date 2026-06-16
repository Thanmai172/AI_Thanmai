from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

conversation_history = []
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

    global conversation_history

    try:

        conversation_history.append({
            "role": "user",
            "content": prompt.message
        })

        response = groq_client.chat.completions.create(
            messages=conversation_history,
            model="llama-3.3-70b-versatile"
        )

        assistant_reply = response.choices[0].message.content

        conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        return {
            "reply": assistant_reply
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )