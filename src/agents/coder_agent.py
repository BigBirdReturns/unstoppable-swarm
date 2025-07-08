# src/agents/coder_agent.py

from src.memory.rehydrate import rehydrate_context
from src.agents.llm import LocalLLM

class CoderAgent:
    """
    A coding agent that uses vector memory to build a contextual prompt,
    then runs that prompt through a local LLM to produce an answer.
    """

    def __init__(self, name="Coder"):
        self.name = name
        self.role = "code_generator"
        self.llm = LocalLLM()

    def generate_code(self, task_description: str) -> str:
        """
        Retrieves relevant context, builds a prompt, and generates a code/response.
        
        :param task_description: The subtask or coding prompt.
        :return: LLM-generated answer.
        """
        prompt = rehydrate_context(task_description)
        output = self.llm.complete(prompt)
        return output
