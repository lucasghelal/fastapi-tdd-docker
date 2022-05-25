import os

import pytest
from starlette.testclient import TestClient

from api.main import create_application
from api.config import get_settings, Settings


def get_setting_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_setting_override
    with TestClient(app) as test_client:
        
        yield test_client