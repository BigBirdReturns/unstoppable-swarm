# src/orchestrator/orchestrator.py

from src.orchestrator.agent_interface import load_agent

class Orchestrator:
    """
    Coordinates multiple agents to execute a swarm-style task pipeline.
    """

    def __init__(self):
        self.planner = load_agent("planner")
        self.coder = load_agent("coder")
        self.verifier = load_agent("verifier")

    def run(self, user_task: str) -> None:
        """
        Runs a full pipeline: plan → code → verify.

        :param user_task: High-level task to decompose and execute.
        """
        print(f"[Swarm Orchestrator] Planning task: {user_task}")
        subtasks = self.planner.plan(user_task)

        for subtask in subtasks:
            step = subtask["step"]
            description = subtask["description"]
            print(f"\n[Step {step}] ➤ {description}")

            code = self.coder.generate_code(description)
            print(f"[Coder Output]\n{code}")

            verdict = self.verifier.verify(code)
            print(f"[Verifier]: {verdict}")
