# testing REST APIs using Google maps api
import requests
import json

request = requests.get('https://api.github.com/events', params= "repo" )
print(request.status_code)
print(request.text)



