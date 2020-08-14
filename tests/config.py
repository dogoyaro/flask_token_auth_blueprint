class UserClassStub:
    @staticmethod
    def create_user(content):
        return content

    @classmethod
    def get_token_payload(_, user):
        return user

    @staticmethod
    def authenticate(user):
        return user


test_config = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:////tmp/test.db',
    'DEBUG': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'USER_MODEL': UserClassStub,
    'SECRET_KEY': 'test secret key',
}
