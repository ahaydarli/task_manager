class TestAuthSignupController:
    def test__post(self, client):
        data = {
            "name": "Darth Vader",
            "email": "foobar@mail.com",
            "password": "123456"
        }
        response = client.post('/api/v1/signup', data=data, content_type='application/json')
        print(response)
        assert response.status_code == 400
