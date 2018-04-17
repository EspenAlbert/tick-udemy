import requests

url = "http://localhost:8086/query"

payload = "q=CREATE%20DATABASE%20tick_udemy"
headers = {
    'content-type': "application/x-www-form-urlencoded"
}
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)