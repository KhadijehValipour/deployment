import requests

url = "https://api.dictionaryapi.dev/api/v2/entries/en/hello"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
