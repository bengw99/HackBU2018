import google.oauth2.credentials
import google_auth_oauthlib.flow

class Auther():
	flow = None 
	auth_url = None 
	
	def __init__(self):
		# Creates a flow
		self.flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
					'client_secret.json',
					scopes=['https://mail.google.com'],
					redirect_uri = 'http://localhost:5000/email/')

		# Tells user where to go
		self.auth_url, _ = self.flow.authorization_url(prompt="consent")
		
	def get_auth_url(self):
		return self.auth_url

    def get_flow(self):
        return self.flow
		
def make_auther():
	auther = Auther()
	return auther