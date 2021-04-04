from flask_jwt_extended import create_refresh_token


class TestAuthRefreshController:
    def test__post(self, client):
        access_token = create_refresh_token('foobar@mail.com')
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        response = client.post('/api/v1/refresh', data={}, headers=headers)
        print(response)
        assert response.status_code == 200
