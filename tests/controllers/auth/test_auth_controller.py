class TestAuthController:
    def test__post(self, client):
        data = {
            "email": "foobar@mail.com",
            "password": "123456"
        }
        response = client.post('/api/v1/auth', data=data, content_type='application/json')
        print(response)
        assert response.status_code == 200
