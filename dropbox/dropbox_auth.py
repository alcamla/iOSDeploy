import urllib
from .dropbox_connection import *
from .dropbox_util import *

class DropboxAuth():
    def __init__(self, app_key, app_secret, prefix_path=None):
        self.connection = DropboxConnection(prefix_path)
        self.app_key = app_key
        self.app_secret = app_secret

    def get_authorize_url(self):
        return DropboxUtil.build_url(DropboxUtil.WEB_HOST, "/oauth2/authorize", False, {"response_type": "code", "client_id": self.app_key})

    def authorize(self, code):
        url = DropboxUtil.build_url(DropboxUtil.API_HOST, "/oauth2/token", False)
        params = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.app_key,
            "client_secret": self.app_secret
        }
        response = self.connection.post(url, params=params)
        access_token = response["access_token"]
        user_id = response["account_id"]
        return access_token, user_id
