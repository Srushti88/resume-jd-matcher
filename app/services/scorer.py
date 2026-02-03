import numpy as np


class SimilarityScorer:
    """
    Responsible only for calculating similarity score between two embeddings.
    """

    @staticmethod
    def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)

        # Avoid division by zero
        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0

        similarity = dot_product / (norm_vec1 * norm_vec2)
        return similarity

    @staticmethod
    def get_match_score(vec1: np.ndarray, vec2: np.ndarray) -> int:
        similarity = SimilarityScorer.cosine_similarity(vec1, vec2)

        # Convert similarity (-1 to 1) into percentage
        score = similarity * 100

        # Clamp score between 0 and 100 for meaningful display
        score = max(0, min(100, int(score)))

        return score
