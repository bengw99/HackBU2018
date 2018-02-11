import google.oauth2.credentials
import google_auth_oauthlib.flow

def start_auth():
    # Creates a flow
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                'client_secret.json',
                scopes=['https://www.googleapis.com/auth/gmail'],
                redirect_uri = 'http://localhost:5000/email/')

    # Tells user where to go
    auth_url, _ = flow.authorization_url(prompt="consent")

    print("Please go to this URL: {}".format(auth_url))

    # Provides user with authorization code and then an access token
    code = input("Enter the authorization code: ")
    flow.fetch_token(code = code)

    # Use flow.authorized_session
    session = flow.authorized_session()
    print(session.get("https://googleapis.com/userinfo/v2/me").json())
