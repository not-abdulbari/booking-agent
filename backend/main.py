from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent.langgraph_agent import run_conversation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_input = data.get("input")
        if not user_input:
            return {"error": "Missing input"}

        response = run_conversation(user_input)
        return {"response": response}
    except Exception as e:
        return {"error": f"❌ Backend crashed: {str(e)}"}