# src/memory/ingest.py

from src.memory.vector_store import VectorStore

def main():
    store = VectorStore()

    # Example doctrine fragments (normally you'd extract from PDF or text files)
    docs = [
        "Spectra collapse refers to compressing knowledge into latent embeddings.",
        "Rehydration is the expansion of compact data into full explanation via LLMs.",
        "The system is designed to operate locally with no cloud dependencies.",
        "Trustless agents must sign their output and store it in an audit log.",
        "Semantic drift tracking ensures the output stays on-topic and aligned."
    ]

    ids = [f"doc{i+1}" for i in range(len(docs))]
    store.add_documents(texts=docs, ids=ids)

    print(f"Ingested {len(docs)} documents into vector memory.")

if __name__ == "__main__":
    main()
