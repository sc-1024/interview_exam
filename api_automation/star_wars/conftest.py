import json
import pytest
from pathlib import Path


def load_json(file_name):
    data_dir = Path(__file__).parent / 'data'
    file_path = data_dir / f"{file_name}.json"
    with file_path.open() as f:
        return json.load(f)


@pytest.fixture
def get_data():
    def _get_data(file_name) -> dict:
        return load_json(file_name)
    return _get_data
