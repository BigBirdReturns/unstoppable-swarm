# src/memory/vector_store.py

import chromadb
from chromadb.utils import embedding_functions

class VectorStore:
    """
    Wrapper around Chroma vector DB for storing and retrieving documents using embeddings.
    Compatible with updated Chroma client and strict include options.
    """

    def __init__(self, persist_path="vector_db", collection_name="swarm_docs"):
        self.client = chromadb.PersistentClient(path=persist_path)
        self.collection_name = collection_name
        self.embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        try:
            self.collection = self.client.get_collection(name=collection_name)
        except:
            self.collection = self.client.create_collection(
                name=collection_name,
                embedding_function=self.embedder
            )

    def add_documents(self, texts: list, ids: list):
        """
        Add text chunks to the vector store.
        :param texts: List of string docs
        :param ids: List of unique string IDs
        """
        self.collection.add(documents=texts, ids=ids)

    def query(self, query_text: str, top_k=3):
        """
        Retrieve top_k most similar docs to query_text.
        :param query_text: The input string to search with.
        :return: List of (doc_id, doc_text) tuples.
        """
        results = self.collection.query(
            query_texts=[query_text],
            n_results=top_k,
            include=["documents"]  # <-- minimal valid option
        )
        docs = results["documents"][0]
        # Fallback fake IDs (doc1, doc2, ...) since we can't fetch real ones
        doc_ids = [f"doc{i+1}" for i in range(len(docs))]
        return list(zip(doc_ids, docs))
