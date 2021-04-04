from flask_jwt_extended import create_refresh_token, create_access_token


class TestUserController:
    def test__get(self, client):
        access_token = create_access_token('foobar@mail.com')
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        response = client.get('/api/v1/user', headers=headers)
        print(response)
        assert response.status_code == 200
