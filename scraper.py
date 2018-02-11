from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import google.oauth2.credentials
import google_auth_oauthlib.flow

from auth import *

def scrape(code):
	auther = Auther()
	auther.get_flow().fetch_token(code = code)
	session = auther.get_flow().authorized_session()
	messages = session.get("https://www.googleapis.com/gmail/v1/users/me/messages").json()
	return messages
