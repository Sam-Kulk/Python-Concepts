import requests

url = 'https://reqres.in/api/login'
a = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
response_object = requests.post(url,json=a,timeout=2.5) # Here this json parameter will convert the dict to JSON string
print(response_object.status_code)

response_json = response_object.json() # The json() will return in the form of dict
print(response_json)
print(response_json['token'])

