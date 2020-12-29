import requests
import simplejson as json

#fetch access_token & refresh_token from Azure table storage
url = "https://<storage_account_name>.table.core.windows.net/<table_name><shared_access_signature_of_the_table>"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
result= json.loads(response.text)

access_token=result.get('value')[0]['access_token']
refresh_token=result.get('value')[0]['refresh_token']


#get new access_token & refresh_token from accelo
grant_type="refresh_token"
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

print('access_token : '+access_token+'\nrefresh_token : '+refresh_token)

con='\"'
at = con + access_token + con
rt = con + refresh_token + con


#store the latest acess_token & refresh_token in Azure table storage
url = "https://<storage_account_name>.table.core.windows.net/<table_name>(PartitionKey='',RowKey='')<shared_access_signature>"

payload="{\r\n    \"access_token\" : " + at + ",\r\n    \"refresh_token\" : " + rt + "\r\n}"
headers = {
  'Content-Type': 'application/json',
  'If-Match': '*'
}

response = requests.request("PUT", url, headers=headers, data=payload)



