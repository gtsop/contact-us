import os
import copy
import pytest

from .settings import Settings

@pytest.fixture
def os_vars():
    original_vars = copy.deepcopy(os.environ)
    yield
    os.environ.clear()
    os.environ.update(original_vars)

def test_settings_instantiates():
    assert Settings()

def test_settings_storage_strategy():
    os.environ['storage_strategy'] = 'in-memory'
    settings = Settings()
    assert settings.storage_strategy == 'in-memory'

    os.environ['storage_strategy'] = 'database'
    settings = Settings()
    assert settings.storage_strategy == 'database'