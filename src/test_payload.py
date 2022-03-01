import payload
from unittest import mock

@mock.patch('time.time', mock.MagicMock(return_value=1))
def test_create__auth_payload():
    payloadCreator = payload.PayloadCreator(
        private_key='abcd', public_key='1234')
    # example from MarvelAPI
    assert payloadCreator.create_auth_payload() == {'ts': 1, 'apikey': '1234', 'hash': 'ffd275c5130566a2916217b101f26150'}
