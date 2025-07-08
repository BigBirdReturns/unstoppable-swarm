# src/orchestrator/agent_interface.py

from src.agents.planner_agent import PlannerAgent
from src.agents.coder_agent import CoderAgent
from src.agents.verifier_agent import VerifierAgent

AGENT_REGISTRY = {
    "planner": PlannerAgent,
    "coder": CoderAgent,
    "verifier": VerifierAgent,
}

def load_agent(role_name: str):
    """
    Dynamically load an agent class by role name.
    
    :param role_name: "planner", "coder", or "verifier"
    :return: an initialized agent instance
    """
    agent_class = AGENT_REGISTRY.get(role_name.lower())
    if agent_class is None:
        raise ValueError(f"Unknown agent role: {role_name}")
    return agent_class()
