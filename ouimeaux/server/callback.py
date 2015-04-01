import requests
import json

class WebCallback:
    def __init__(self,device,url,user,password):
        self.device = device
        self.url = url
        self.user = user
        self.password = password
        print 'registered callback to: ', self.url
        
    def doCallback(self,state):
        print 'setting ', self.device.serialnumber,' state to ',state
        # build payload
        data = {
            'device_state': state,
            'device_serial_number': self.device.serialnumber
        }
        
        # Set proper headers
        headers = {"Content-Type":"application/json","Accept":"application/json"}

        # Do the HTTP request
        response = requests.post(self.url, auth=(self.user, self.password), headers=headers ,data=json.dumps(data))

        # Check for HTTP codes other than 201
        if response.status_code != 201:
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        else:
            # Decode the JSON response into a dictionary and use the data
            data = response.json()
            print(data)

    @property
    def url(self):
        return self.url
    @property
    def user(self):
        return self.user
