import requests
import json

reqUrl = "http://127.0.0.1:8000/"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "Content-Type": "application/json" 
}

payload = json.dumps({
    "title": "No Title",
    "length": "4.03",
    "artist": "Reol"
})

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)