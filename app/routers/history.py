from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict

from .. import crud
from ..database import get_db

router = APIRouter(
    prefix="/api/v1/history",
    tags=["History"],
)

@router.delete("/{item_id}", response_model=Dict[str, str])
def delete_single_history_item(item_id: int, db: Session = Depends(get_db)):
    """
        dELETE with ID
    """
    deleted_item = crud.delete_history_item_by_id(db, item_id=item_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="آیتم مورد نظر یافت نشد.")
    return {"message": "آیتم با موفقیت حذف شد."}


@router.delete("/clear-all", response_model=Dict[str, str])
def delete_all_history_items(db: Session = Depends(get_db)):
    """
    کل تاریخچه تحلیل‌ها را حذف می‌کند.
    """
    rows_deleted = crud.delete_all_history(db)
    return {"message": f"{rows_deleted} آیتم با موفقیت حذف شد."}
