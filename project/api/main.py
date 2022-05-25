import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.router import ping


def create_application() -> FastAPI:
    application = FastAPI(version='0.0.3')

    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["api.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )
    
    application.include_router(ping.router)

    return application


app = create_application()
