from app.services.embedder import TextEmbedder
from app.services.scorer import SimilarityScorer


class ResumeJDMatcher:

    def __init__(self):
        self.embedder = TextEmbedder()
        self.scorer = SimilarityScorer()

    def calculate_match(self, resume_text: str, jd_text: str) -> int:
        resume_embedding = self.embedder.get_embedding(resume_text)
        jd_embedding = self.embedder.get_embedding(jd_text)

        score = self.scorer.get_match_score(resume_embedding, jd_embedding)
        return score
