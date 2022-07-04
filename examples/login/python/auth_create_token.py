import http.client
import json
from datetime import datetime, timedelta
import requests

conn = http.client.HTTPSConnection("login.smartcoach.club")

dev_audience = 'https://api.dev.brainanalytics.co'
stage_audience = 'https://api.stage.brainanalytics.co'
prod_audience = 'https://api.prod.brainanalytics.co'

payload = {
    'client_id': 'xxx',
    'client_secret': 'xxx',
    'audience': prod_audience,
    'grant_type': 'client_credentials'
}

headers = {'content-type': "application/json"}

conn.request("POST", "/oauth/token", json.dumps(payload), headers)

res = conn.getresponse()
data = res.read()
response = json.loads(data.decode("utf-8"))
response['access_token'] = 'Bearer ' + response['access_token']

date_start = f'{datetime.now():%Y%m%d}'
date_end = f'{datetime.now() + timedelta(days=1):%Y%m%d}'

match_url = f'https://betting.dev.brainanalytics.co/data/match_list/{date_start}/{date_end}'

match_response = requests.get(
    match_url,
    headers={'accept': 'application/json', 'authorization': response['access_token']}
).json()

print(match_response)
