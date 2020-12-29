#access token using refresh token

import requests
import simplejson as json

grant_type="refresh_token"
refresh_token="enter_refresh_token"

url = "https://<company_name>.api.accelo.com/oauth2/v0/token?grant_type="+grant_type+"&refresh_token="+refresh_token

payload={}
headers = {
  'Authorization': 'Basic enter_base64_encoded',
  'Cookie': 'al_domain=enter_domain_name'
}

response = requests.request("POST", url, headers=headers, data=payload)

result= json.loads(response.text)

access_token=result['access_token']
refresh_token=result['refresh_token']


print("access_token:",access_token)
print("refresh_token:",refresh_token)
