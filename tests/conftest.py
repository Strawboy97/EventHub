import json
import os.path

import pytest

from pages.home import HomePage
from pages.login import LoginPage


@pytest.fixture
def create_user_data(faker):
    data = {"email": faker.email(), "password": faker.password()}

    file_path = "userData.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing_file = json.load(f)
    else:
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    existing_file.append(data)

    with open(file_path, "w") as f:
        json.dump(existing_file, f, indent=2)

    return data


@pytest.fixture
def read_user_data():
    file_path = "userData.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing_file = json.load(f)
    else:
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    data = existing_file[0]
    return data


@pytest.fixture
def login_user(page, read_user_data):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.login(read_user_data['email'], read_user_data['password'])

    home_page = HomePage(page)
    return home_page
