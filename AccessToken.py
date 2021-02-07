import base64
import requests
import datetime

client_id = '5ee7a648878b46cfb5f4c973736acc99'
client_secret = 'ff39b32792fa4603b830accb294bf433'
redirect_url = 'http://localhost:8000'

client_creds = f"{client_id}:{client_secret}"
type (client_creds)

client_creds_b64 = base64.b64encode(client_creds.encode())
type(client_creds_b64)


token_url = 'https://accounts.spotify.com/api/token'
method = "POST"
token_data = {
    "grant_type": "client_credentials"
}
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}" # <base64 encoded client_id:client_secret>
}

r = requests.post(token_url, data=token_data, headers=token_headers)
print(r.json())
valid_request = r.status_code in range(200, 299)
token_response_data = r.json()

if valid_request:
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in']
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now