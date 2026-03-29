from env.environment import CustomerSupportEnv
from env.models import Action

env = CustomerSupportEnv()

def reset():
    obs = env.reset()
    return {
        "observation": {
            "customer_query": obs.customer_query,
            "conversation_history": obs.conversation_history,
            "ticket_status": obs.ticket_status,
            "sentiment": obs.sentiment,
            "progress": float(obs.progress)
        }
    }

def step(action: dict):
    action_obj = Action(**action)

    obs, reward, done, info = env.step(action_obj)

    return {
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
    }
