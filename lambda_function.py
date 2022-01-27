import http.client
import json

def lambda_handler(event, context):
    
    #format data from message text
    temp_data = float(event['temperature'])
    
    if temp_data > 24.0: # You can change the value as per your use case
      conn = http.client.HTTPSConnection("api.telnyx.com")
      payload = json.dumps({
      "from": "TELNYX_PHONE_NUMBER", # Obtain number from portal.telnyx.com
      "to": "YOUR_PHONE_NUMBER",
      "text": "The temperature is "+ str(temp_data) + " degree celsius" # A text you will receive on YOUR_PHONE_NUMBER
      })
      headers = {
      'Content-Type': 'application/json',
      'Authorization': 'TELNYX_API_KEY'
      }
      conn.request("POST", "/v2/messages", payload, headers)
