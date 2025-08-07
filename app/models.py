import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class AnalysisHistory(Base):
    __tablename__ = "analysis_history"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
    score = Column(Float, nullable=False)
    analyzed_at = Column(DateTime, default=datetime.datetime.utcnow)
