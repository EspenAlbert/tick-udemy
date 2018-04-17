import requests

url = "http://localhost:8086/query"

querystring = {"pretty": "true", "db": "tick_udemy",
               "q": "SELECT \"temperature\" FROM \"sensors\" WHERE \"sensor_id\"='climax_1531'"}

response = requests.request("GET", url, params=querystring)

print(response.text)
