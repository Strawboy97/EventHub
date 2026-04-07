import pytest


@pytest.fixture
def user_data(faker):
    data = {'email': faker.email(), 'password': faker.password()}

    with open('userdata.txt', 'a') as f:
        f.write(f'{data['email']}:{data['password']}\n')

    return data
