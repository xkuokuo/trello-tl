import configparser

class CredentialProvider:
    """Class providing trello api credentials"""

    def __init__(self, credential_file_path):
        print("Loading credential from config: {}".format(credential_file_path))
        config = configparser.ConfigParser()
        config.read(credential_file_path)
        self.access_key = config['Credential']['access_key']
        self.token = config['Credential']['token']

    def get_access_key(self):
        return self.access_key

    def get_token(self):
        return self.token

