import json

import pytest


@pytest.fixture
def user_data(faker):
    data = {'email': faker.email(), 'password': faker.password()}

    existing_file = json.load(open('userData.json', 'r'))

    existing_file.append(data)

    json.dump(existing_file, open('userData.json', 'w'))

    return data
