import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        self.headers ={
            "Content-Type": "application/json"
        }
    
    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response
    
    def post(self, endpoint, payload):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, json=payload, headers=self.headers)
        return response
    
    def put(self, endpoint, payload):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, json=payload, headers=self.headers)
        return response
    
    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response