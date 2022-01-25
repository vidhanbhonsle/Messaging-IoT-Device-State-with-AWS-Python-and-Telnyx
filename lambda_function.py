import http.client
import json

def lambda_handler(event, context):
    
    #format data from message text
    temp_data = float(event['temperature'])
    
    if temp_data > 22.0:
      conn = http.client.HTTPSConnection("api.telnyx.com")
      payload = json.dumps({
      "from": "TELNYX_NUMBER",
      "to": "YOUR_NUMBER",
      "text": "The temperature is "+ str(temp_data) + " degree celsius"
      })
      headers = {
      'Content-Type': 'application/json',
      'Authorization': 'YOUR_API_KEY'
      }
      conn.request("POST", "/v2/messages", payload, headers)