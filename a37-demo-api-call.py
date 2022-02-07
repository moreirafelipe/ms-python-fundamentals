#use the requests library to simplify making a REST API call from Python
import requests
import json

#We will need the json lirary to read the data passed back by the web service
SUBSCRIPTION_KEY = "12f4b7ef2a344a9b8b9bc4586ebf6ec9"

#Computer vision service endpoint address
vision_service_address = "https://pythonimageanalyzer3.cognitiveservices.azure.com/"

#Add tha name of the function we want to call to the address
address = vision_service_address + "analyze"

parameters = {'visualFeatures':'Description, Color', 'language':'en'}

#Calling the image
image_path = "./images/paris.jpeg"
image_data = open(image_path, "rb").read()

#Passing the access key
headers = {'Content-Type': 'application/octet-stream',
           'Ocp_Apim-Subscription-Key': SUBSCRIPTION_KEY}

#Using HTTP POST to call the function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

#Exception for ewrror return
response.raise_for_status()

#Display the JSON results returned
results = response.json()
print(json.dumps(results))

#Print the JSON output
print()
print('requestId')
print(results['requestId'])