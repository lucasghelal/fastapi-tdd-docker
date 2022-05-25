import logging

from fastapi import FastAPI

from api.router import ping, summaries
from api.db import init_db


log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI(version='0.0.3')        
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix="/summaries", tags=["summaries"])
    
    return application

app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")