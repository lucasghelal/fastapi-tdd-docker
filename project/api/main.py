from fastapi import Depends, FastAPI

from api.config import get_settings, Settings


app = FastAPI(
    version='0.0.2'
)

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {'ping': 'pong!',
            'enviroment': settings.environment,
            'testing': settings.testing
    }
