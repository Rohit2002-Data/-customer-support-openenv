from fastapi import FastAPI
from env.environment import CustomerSupportEnv
from env.models import Action

app = FastAPI()
env = CustomerSupportEnv()


@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "observation": obs.model_dump()
    }

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs.model_dump(),
        "reward": reward,
        "done": done,
        "info": info
    }
