class CredentialProvider:
    """Class providing trello api credentials"""

    def __init__(self, config):
        self.access_key = config['access_key']
        self.token = config['token']

    def get_access_key(self):
        return self.access_key

    def get_token(self):
        return self.token

