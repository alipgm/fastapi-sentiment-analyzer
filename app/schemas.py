import datetime
from pydantic import BaseModel

class AnalysisBase(BaseModel):
    text: str

class AnalysisResultBase(BaseModel):
    sentiment: str
    score: float

class AnalysisRequest(AnalysisBase):
    pass

class AnalysisResponse(AnalysisBase, AnalysisResultBase):
    pass

class AnalysisHistory(AnalysisResponse):
    id: int
    analyzed_at: datetime.datetime

    class Config:
        from_attributes = True
