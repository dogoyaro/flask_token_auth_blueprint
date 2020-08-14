from unittest.mock import patch, Mock
from .base import BaseTestCase
from ..resource import auth_blueprint


class TestResource(BaseTestCase):
    @patch('token_auth.resource.generate_token')
    def test_register_user_resource(self, generate_token_mock):
        generate_token_mock.return_value = b'1234'
        user = {'username': 'tester', 'password': 'testpassword'}
        response = self.client.post('/token-register', json=user)
        assert(response.get_json()['token']) == '1234'

    @patch('token_auth.resource.generate_token')
    def test_authenticate_user_resource(self, generate_token_mock):
        generate_token_mock.return_value = b'1234'
        user = {'email': 'tester', 'password': 'testpassword'}
        response = self.client.post('/token-login', json=user)
        assert(response.get_json()['token']) == '1234'

