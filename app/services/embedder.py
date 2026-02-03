from sentence_transformers import SentenceTransformer
import numpy as np


class TextEmbedder:
    """
    Responsible only for converting text into embeddings.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def get_embedding(self, text: str) -> np.ndarray:
        embedding = self.model.encode(text)
        return np.array(embedding)
