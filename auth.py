import google.oauth2.credentials
import google_auth_oauthlib.flow

class Auther(object):
	flow
	auth_url
	
	def __init__():
		# Creates a flow
		flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
					'client_secret.json',
					scopes=['https://mail.google.com'],
					redirect_uri = 'http://localhost:5000/email/')

		# Tells user where to go
		auth_url, _ = flow.authorization_url(prompt="consent")
		
	def get_auth_url():
		return auth_url
		
def make_auther():
	auther = Auther()
	return auther
	
	

"""
    # Provides user with authorization code and then an access token
    code = input("Enter the authorization code: ")
    flow.fetch_token(code = code)

    # Use flow.authorized_session
    session = flow.authorized_session()
    print(session.get("https://googleapis.com/userinfo/v2/me").json())
"""
