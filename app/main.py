from fastapi import FastAPI, HTTPException
from bedrock_lib import invoke_claude, save_chat, ChatRequest, ChatResponse

app = FastAPI(title="Bedrock Chat API")

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message is required")

    reply = invoke_claude(request.message)
    save_chat(request.message, reply)
    return ChatResponse(reply=reply)
