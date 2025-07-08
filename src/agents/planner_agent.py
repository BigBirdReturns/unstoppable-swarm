import re
from typing import List, Dict

class PlannerAgent:
    """
    A simple planning agent that takes a user task and returns a list of structured subtasks.
    This version does not call a language model yet — it's a stub for orchestrator integration.
    """

    def __init__(self, name="Planner"):
        self.name = name
        self.role = "task_decomposer"

    def plan(self, task_description: str) -> List[Dict]:
        """
        Decomposes a user task into subtasks using simple rule-based splitting.
        This will later be replaced with LLM logic.

        :param task_description: A string describing the user’s goal or task.
        :return: A list of subtask dicts with step IDs and descriptions.
        """
        # Basic placeholder: split by punctuation or connector words
        # Later this will be replaced with LLM reasoning
        steps = re.split(r"[.;\n]| and then | then ", task_description, flags=re.IGNORECASE)
        subtasks = []

        for i, step in enumerate(steps):
            cleaned = step.strip()
            if cleaned:
                subtasks.append({
                    "step": i + 1,
                    "description": cleaned
                })

        return subtasks
