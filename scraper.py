from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://mail.google.com'
CLIENT_SECRET = 'client_secret.json'

class Sender(object):
	

def get_credentials():
	store = file.Storage('storage.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
		creds = tools.run_flow(flow, store)
	return creds
	
def scrape():
	credentials = get_credentials()
	GMAIL = build('gmail', 'v1', http=credentials.authorize(Http()))
	messages = service.users().messages().list(userId=me, q='in:inbox').execute().get(
	for message in messages
		