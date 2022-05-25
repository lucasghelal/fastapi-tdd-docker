import os

from fastapi import Depends, FastAPI
from tortoise.contrib.fastapi import register_tortoise

from api.config import get_settings, Settings


app = FastAPI(
    version='0.0.2'
)

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["api.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {'ping': 'pong!',
            'enviroment': settings.environment,
            'testing': settings.testing
    }
