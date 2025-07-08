# src/memory/rehydrate.py

from src.memory.vector_store import VectorStore

def rehydrate_context(query: str, top_k=3) -> str:
    """
    Retrieves relevant context fragments for a given query and constructs a prompt.
    
    :param query: User task or subtask.
    :param top_k: Number of chunks to retrieve.
    :return: Prompt string with retrieved context included.
    """
    store = VectorStore()
    retrieved = store.query(query, top_k=top_k)

    context_lines = []
    for idx, (doc_id, doc_text) in enumerate(retrieved, 1):
        context_lines.append(f"[{idx}] {doc_text.strip()}")

    context_block = "\n".join(context_lines)
    prompt = (
        f"You are a helpful AI agent. Use the following context to assist the task.\n\n"
        f"---\n{context_block}\n---\n\n"
        f"Task: {query}\nAnswer:"
    )

    return prompt
