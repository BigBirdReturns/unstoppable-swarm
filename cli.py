# cli.py

from src.orchestrator.orchestrator import Orchestrator

def main():
    print("=== Unstoppable v2 CLI ===")
    user_task = input("Enter a high-level task for the swarm:\n> ").strip()
    if not user_task:
        print("No task provided. Exiting.")
        return

    orchestrator = Orchestrator()
    orchestrator.run(user_task)

if __name__ == "__main__":
    main()

