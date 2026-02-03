from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    match_score: int
    analysis: str
