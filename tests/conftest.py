import os
from dotenv import load_dotenv
import pytest
load_dotenv()

from klarda import KlardaAPICollection

@pytest.fixture
def api_key() -> str:
    key = os.environ.get("KLARDA_API_KEY")
    assert key
    return key

@pytest.fixture
def client(api_key: str) -> KlardaAPICollection:
    return KlardaAPICollection(api_key)