import time
import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from dotenv import load_dotenv

#upload variable -> .env
load_dotenv()

from .database import engine, Base
from .routers import analysis, pages, history 

@asynccontextmanager
async def lifespan(app: FastAPI):
    #(startup)
    with open('server_log.log', 'a', encoding='utf-8') as log:
        log.write(f'--- Application startup at {datetime.datetime.now()} ---\n')
    
    yield 
    
    #(shutdown)
    with open('server_log.log', 'a', encoding='utf-8') as log:
        log.write(f'--- Application shutdown at {datetime.datetime.now()} ---\n')


app = FastAPI(
    title="Sentim-API",
    description="یک API هوشمند برای تحلیل احساسات متن با ساختاری حرفه‌ای",
    version="1.0.0",
    lifespan=lifespan
)

#Middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(round(process_time, 4))
    return response

app.include_router(analysis.router)
app.include_router(pages.router)
app.include_router(history.router) 

@app.get("/health", tags=["Health Check"])
def health_check():
    """یک اندپوینت ساده برای بررسی سلامت سرور."""
    return {"status": "ok", "message": "Server is healthy"}
