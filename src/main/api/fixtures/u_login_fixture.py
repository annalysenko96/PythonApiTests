import pytest

from src.main.api.configs.config import Config
from src.main.api.specs.request_specs import RequestSpecs


@pytest.fixture
def user_login(api_manager, create_user_request):
    login = {"headers": RequestSpecs.auth_headers(
        create_user_request.username,
        create_user_request.password
    ),
        "base_url": Config.fetch("backendUrl")
    }
    return login