
import random
from .models import Observation, Action
from .tasks import TASKS
from .grader import grade

class CustomerSupportEnv:

    def __init__(self):
        self.task = None
        self.history = []
        self.steps = 0
        self.status = "open"
        self.progress = 0.0

    def reset(self):
        self.task = random.choice(list(TASKS.values()))
        self.history = []
        self.steps = 0
        self.status = "open"
        self.progress = 0.0

        return Observation(
            customer_query=self.task["query"],
            conversation_history=[],
            ticket_status=self.status,
            sentiment="negative",
            progress=0.0
        )

    def step(self, action: Action):
        self.steps += 1

        score, feedback = grade(action, self.task, self.steps)

        # loop penalty
        if self.history:
            last = self.history[-1]["agent"]
            if last["action_type"] == action.action_type:
                score -= 0.1

        self.progress = (self.progress + score) / 2

        done = score > 0.75 or self.steps >= 5

        if done:
            self.status = "closed"

        self.history.append({"agent": action.model_dump()})

        obs = Observation(
            customer_query=self.task["query"],
            conversation_history=self.history,
            ticket_status=self.status,
            sentiment="neutral" if done else "negative",
            progress=self.progress
        )

        return obs, max(0, min(1, score)), done, {"feedback": feedback}

    def state(self):
        return {
            "task": self.task,
            "history": self.history,
            "steps": self.steps,
            "progress": self.progress
        }
