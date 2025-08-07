from sqlalchemy.orm import Session
from . import models, schemas

def create_analysis_record(db: Session, analysis_data: schemas.AnalysisResponse):
    """
    save one record in db
    """
    db_record = models.AnalysisHistory(
        text=analysis_data.text,
        sentiment=analysis_data.sentiment,
        score=analysis_data.score,
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_analysis_history(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AnalysisHistory).order_by(models.AnalysisHistory.id.desc()).offset(skip).limit(limit).all()


def delete_history_item_by_id(db: Session, item_id: int):
    db_item = db.query(models.AnalysisHistory).filter(models.AnalysisHistory.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
        return db_item
    return None

def delete_all_history(db: Session):
    rows_deleted = db.query(models.AnalysisHistory).delete()
    db.commit()
    return rows_deleted
