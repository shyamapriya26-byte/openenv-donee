# env.py
import random
from models import Observation
from tasks import TASKS, ISSUES  
from grader import grade_internet_not_working, grade_slow_laptop, grade_wifi_disconnecting

class SupportEnv:
    def __init__(self):
        self.current_issue = None
        self.current_path = []
        self.current_step = 0
        self.steps_taken = 0
        self.agent_actions = []   

    def reset(self, *, seed=None, options=None):
        """
        Reset the environment.
        If options contains 'task_id', use that task; otherwise pick a random one.
        """
        # Determine which task to run
        if options and "task_id" in options:
            task_id = options["task_id"]
            
            self.current_issue = task_id
            self.current_path = random.choice(ISSUES[task_id])
        else:
            # fallback to random easy task
            self.current_issue = random.choice(TASKS["easy"])
            self.current_path = random.choice(ISSUES[self.current_issue])

        self.current_step = 0
        self.steps_taken = 0
        self.agent_actions = []
        return self.state()

    def state(self):
        return Observation(
            issue=self.current_issue,
            current_step=self.current_step,
            steps_taken=self.steps_taken
        )

    def step(self, action):

        self.agent_actions.append(action)

        correct_action = self.current_path[self.current_step]
        
        from grader import grade_action
        reward = grade_action(action, correct_action)

        self.steps_taken += 1

        if reward == 1.0:
            self.current_step += 1

        done = self.current_step >= len(self.current_path)

        # efficiency scoring
        if done:
            if self.steps_taken == len(self.current_path):
                reward = min(1.0, reward + 0.2)
            else:
                reward = max(0.0, reward - 0.2)

        if not done:
            next_state = self.current_path[self.current_step]
        else:
            next_state = "resolved"

        return next_state, reward, done, {}
