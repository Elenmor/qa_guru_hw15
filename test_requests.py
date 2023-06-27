import requests


def test_create_new_user():
    name = 'morpheus'
    job = 'leader'
    response = requests.post(url='https://reqres.in/api/users/',
                             json={
                                 "name": name,
                                 "job": job
                             }
                             )

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_page():
    response = requests.get(url='https://reqres.in/api/users?page=2')
    assert response.json()['page'] == 2
    assert len(response.json()['data']) == 6
    assert response.status_code == 200


def test_update_user():
    user_id = 2
    name = 'morpheus'
    job = 'zion resident'
    response = requests.put(url='https://reqres.in/api/users/{user_id}',
                            json={
                                "name": name,
                                "job": job
                            }
                            )

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_update_user_email():
    user_id = 9
    email = 'test@test.ru'
    response = requests.put(url='https://reqres.in/api/users/{user_id}',
                            json={
                                "email": email,
                            }
                            )

    assert response.status_code == 200
    assert response.json()['email'] == email


def test_delete_user():
    user_id = 12
    response = requests.delete(f'https://reqres.in/api/users/{user_id}')

    assert response.status_code == 204


def test_users_json_structure():
    response = requests.get('https://reqres.in/api/users', params={'page': 1})

    assert response.status_code == 200
    assert 'page' in response.json()
    assert 'per_page' in response.json()
    assert 'total_pages' in response.json()
    assert 'total' in response.json()
    assert 'data' in response.json()


def test_user_not_found():
    user_id = 15
    response = requests.get(f'https://reqres.in/api/users/{user_id}')

    assert response.status_code == 404
    assert response.json() == {}


def test_user():
    user_id = 8
    response = requests.get(f'https://reqres.in/api/users/{user_id}')

    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id

def test_authorization_successful():

    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    assert response.status_code == 200
    assert response.text == '{"token":"QpwL5tke4Pnpja7X4"}'


def test_register_user_error():
    response = requests.post(
        url='https://reqres.in/api/register',
        json={
            "email": "sydney@fife"
        }
    )

    assert response.status_code == 400
    assert response.text == '{"error":"Missing password"}'




