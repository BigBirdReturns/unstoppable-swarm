# src/agents/llm.py

from llama_cpp import Llama
import os

# Default to 7B Mistral model in models/ directory
MODEL_PATH = os.getenv("LLM_MODEL_PATH", "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")

class LocalLLM:
    """
    Thin wrapper around llama-cpp for local inference.
    Loads a quantized .gguf model and runs prompt completions offline.
    """

    def __init__(self, model_path=MODEL_PATH, context_size=2048):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"LLM model not found: {model_path}")
        self.model = Llama(model_path=model_path, n_ctx=context_size)

    def complete(self, prompt: str, max_tokens=300, temperature=0.7) -> str:
        output = self.model(
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=["\nUser:", "Task:"],
            echo=False
        )
        return output["choices"][0]["text"].strip()
