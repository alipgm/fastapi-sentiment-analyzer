from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .. import crud
from ..database import get_db

router = APIRouter(
    tags=["Pages"],
)

#templates path
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    history = crud.get_analysis_history(db, limit=10) 
    #Request object for Jinja2 is necessary
    return templates.TemplateResponse("index.html", {"request": request, "history": history})
