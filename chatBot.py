import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv



load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

app = FastAPI(title="AI Chatbot API")

chat_history = []

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    try:
        # Build messages with history
        messages = chat_history + [{"role": "user", "content": req.user_input}]

        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",  
            messages=messages,
            max_tokens=500  
        )

        ai_reply = response.choices[0].message.content

        chat_history.append({"role": "user", "content": req.user_input})
        chat_history.append({"role": "assistant", "content": ai_reply})

        return {"reply": ai_reply}
    except Exception as e:
        return {"error": str(e)}
