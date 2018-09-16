# coding: utf-8
import requests
import json

url = "http://text-processing.com/api/sentiment/"
headers = {}

def getSentiment(sample):
	payload = {"language": "english", "text": sample}
	response = requests.post(url, data = payload, headers = headers)
	##Prints label and status code
	#print(response.status_code)
	#print(json.loads(response.text)["label"])
	return(json.loads(response.text)["label"])
