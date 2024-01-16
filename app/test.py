import requests
import json

def test():
    url = 'http://localhost:8000/items/'
    body = {
        "name": "string",
        "description": "string",
        "price": 0,
        "tax": 0
    }
    response = requests.post(url, json.dumps(body))
    print(response.text)

if __name__ == '__main__':
    test()