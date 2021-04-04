from flask_jwt_extended import create_refresh_token, create_access_token


class TestTaskController:
    def test__post(self, client):
        access_token = create_access_token('foobar@mail.com')
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        data = {
            "ip_address": "114.18.206.215"
        }
        response = client.get('/api/v1/user', data=data, headers=headers)
        print(response)
        assert response.status_code == 200
