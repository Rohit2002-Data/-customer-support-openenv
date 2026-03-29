from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from env.environment import CustomerSupportEnv
from env.models import Action

app = FastAPI()
env = CustomerSupportEnv()

# 🔹 RESET (POST only, strict JSON format)
@app.post("/reset")
def reset(dummy: dict = Body(default={})):
    obs = env.reset()

    return JSONResponse(content={
        "observation": {
            "customer_query": obs.customer_query,
            "conversation_history": obs.conversation_history,
            "ticket_status": obs.ticket_status,
            "sentiment": obs.sentiment,
            "progress": float(obs.progress)
        }
    })


# 🔹 STEP (POST only, strict JSON format)
@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)

    return JSONResponse(content={
        "observation": {
            "customer_query": obs.customer_query,
            "conversation_history": obs.conversation_history,
            "ticket_status": obs.ticket_status,
            "sentiment": obs.sentiment,
            "progress": float(obs.progress)
        },
        "reward": float(reward),
        "done": bool(done),
        "info": info
    })
