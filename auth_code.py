#acces token using authorization code

import requests
import simplejson as json

grant_type="authorization_code"
code="enter_code_here"
redirect_uri="enter_redirect_url"

url = "https://<company_name>.api.accelo.com/oauth2/v0/token?grant_type="+grant_type+"&code="+code+"&redirect_uri="+redirect_uri

payload={}
headers = {
  'Authorization': 'Basic enter_base64_encoded',
  'Cookie': 'al_domain=enter_domain_name'
}

response = requests.request("POST", url, headers=headers, data=payload)

result= json.loads(response.text)

access_token=result['access_token']

try:
	refresh_token=result['refresh_token']
except:
	pass

print("access_token:",access_token)
print("refresh_token:",refresh_token)
