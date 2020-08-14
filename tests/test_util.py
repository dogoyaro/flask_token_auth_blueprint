from unittest.mock import patch, MagicMock, Mock
from ..util import login_required
from .base import BaseTestCase


class TestUtil(BaseTestCase):
    @patch('token_auth.util.jwt')
    @patch('token_auth.util.request')
    def test_login_required_decorator(self, request_mock, jwt_mock):
        jwt_mock.decode = MagicMock(return_value={'id': 1})
        request_mock.headers = { 'Authorization': 'Bearer 1234' }
        def dummy_func():
            return 1

        authed_function = login_required(dummy_func)
        assert(authed_function()) == 1

        # test failed authorization
        jwt_mock.decode = Mock(side_effect=KeyError('some dummy error'))
        request_mock.headers = { 'Authorization': 'Bearer 1234' }

        def dummy_func():
            return 1

        authed_response, _ = login_required(dummy_func)()
        assert(authed_response['message']) == 'Unauthorized'

