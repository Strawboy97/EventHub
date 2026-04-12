import json
import os.path

import pytest


@pytest.fixture
def user_data(faker):
    data = {"email": faker.email(), "password": faker.password()}

    file_path = "userData.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing_file = json.load(f)
    else:
        existing_file = []

    existing_file.append(data)

    with open(file_path, "w") as f:
        json.dump(existing_file, f, indent=2)

    return data
