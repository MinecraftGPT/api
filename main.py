import os
import httpx
import yaml
from collections import deque
from typing import Optional, Dict, List
from fastapi import FastAPI, Request
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# --- Configuration ---
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

# --- Rate Limiting ---
limiter = Limiter(key_func=get_remote_address, default_limits=[config["security"]["rate_limit"]])
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# --- Player Memory ---
player_memory: Dict[str, deque] = {}
MAX_HISTORY = config["memory"]["max_history_size"]

# --- Pydantic Models ---
class ChatRequest(BaseModel):
    player: str
    message: str
    model: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str

# --- API Endpoint ---
@app.post("/chat", response_model=ChatResponse)
@limiter.limit(config["security"]["rate_limit"])
async def chat(request: Request, chat_request: ChatRequest):
    api_key = config["api"]["openrouter_api_key"]
    
    # Determine which model to use
    model_to_use = config["model"]["default_name"]
    if config["model"]["allow_client_override"] and chat_request.model:
        model_to_use = chat_request.model

    if not api_key or api_key == "your_openrouter_api_key":
        return {"reply": "Error: OPENROUTER_API_KEY not configured in config.yml."}
    if not model_to_use:
        return {"reply": "Error: Model name not configured in config.yml."}

    # Prepare conversation history
    system_message = {"role": "system", "content": config["prompt"]["system_message"]}
    
    if chat_request.player not in player_memory:
        player_memory[chat_request.player] = deque(maxlen=MAX_HISTORY * 2) # Store pairs of messages
    
    history = player_memory[chat_request.player]
    
    messages = [system_message] + list(history)
    user_message_content = config["prompt"]["user_template"].format(player=chat_request.player, message=chat_request.message)
    messages.append({"role": "user", "content": user_message_content})

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": model_to_use,
                    "messages": messages,
                    "temperature": config["model"]["temperature"]
                }
            )
            response.raise_for_status()
            data = response.json()
            reply = data["choices"][0]["message"]["content"]

            # Save conversation to memory
            history.append({"role": "user", "content": user_message_content})
            history.append({"role": "assistant", "content": reply})

            return {"reply": reply}
        except httpx.HTTPStatusError as e:
            return {"reply": f"Error: Failed to contact AI service: {e}"}
        except Exception as e:
            return {"reply": f"Error: An unexpected error occurred: {e}"}

# --- Server Startup ---
if __name__ == "__main__":
    import uvicorn
    server_config = config.get("server", {})
    host = server_config.get("host", "0.0.0.0")
    port = server_config.get("port", 8000)
    uvicorn.run(app, host=host, port=port)
