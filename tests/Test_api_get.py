import requests
import json
import jsonpath
from requests.auth import HTTPBasicAuth

base_url = "https://reqres.in/api/"

def test_api_get():
	url= base_url+"users?page=2"
	
	response = requests.get(url)
	assert response.status_code == 200
	
	"""
	#response.content 		-> data in bytes
	#response.text			-> data in unicode
	#response.header		-> to get header
	#response.cookie		-> get cookie
	#response.elapsed		-> time taken by the flow
	"""
	
	json_data = json.loads(response.text)
	first_name = jsonpath.jsonpath(json_data,'data[0].first_name')  #you can use jsonpath.com for quick reference. jsonpath always gives out list.
	assert first_name[0] == "Michael"