import requests
import json
from getpass import getpass

keylen = 40
apikey = getpass(prompt='Enter API key: ').strip()
if (len(apikey) == keylen):
    print('Key length OK (' + str(len(apikey)) + ')')
else:
    print('Key length doesn\'t look right (' + str(len(apikey)) + ')')
print('\n')

def start():
    reg = input('Enter registration: ').strip()
    url = 'https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'
    headers = {
        'x-api-key': apikey,
        'Content-Type': 'application/json'
    }
    cookies = {
        'SESSION_ID': '' 
    }
    data = {
        'registrationNumber': reg
    }

    r = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(data))
    if (r.status_code == 200):
        print(json.dumps(r.json(), indent=4, sort_keys=True).replace('\"', ''))
    else:
        print(r.status_code)
    print('\n')
    
    start()

start()
