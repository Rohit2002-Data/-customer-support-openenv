
import os, json
from openai import OpenAI
from env.environment import CustomerSupportEnv
from env.models import Action

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
env = CustomerSupportEnv()

total = 0

for _ in range(3):
    obs = env.reset()

    prompt = f"""
Return JSON:
{{"category":"","action_type":"","response_text":""}}

Query: {obs.customer_query}
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    try:
        data = json.loads(res.choices[0].message.content)
    except:
        data = {"category":"account","action_type":"respond","response_text":"help"}

    action = Action(**data)
    _, reward, _, _ = env.step(action)
    total += reward

print("Baseline Score:", total/3)
