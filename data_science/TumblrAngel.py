# coding: utf-8
import requests
import json

url = "http://text-processing.com/api/sentiment/"
headers = {}

def getSentiment(sample):
	payload = {"language": "english", "text": sample}
	response = requests.post(url, data = payload, headers = headers)
	#Prints label and status code
	print(response.status_code)
	print(json.loads(response.text)["label"])


getSentiment('I’m going to kill myself, and this isn’t a cry for help. I just need someone to come over here and clean up the mess.')