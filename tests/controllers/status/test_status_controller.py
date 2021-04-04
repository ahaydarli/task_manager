from flask_jwt_extended import create_refresh_token, create_access_token


class TestStatusController:
    def test__post(self, client):
        access_token = create_access_token('foobar@mail.com')
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        task_id = "e0cece05-34dc-4369-86dc-adf333ff3b7f"

        response = client.get(f'/api/v1/status/{task_id}', headers=headers)
        print(response)
        assert response.status_code == 200
