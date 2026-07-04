import requests
import pytest
import uuid
from conftest import load_test_data
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    
def test_create_users(api_client):
    
    """user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }"""
    user_data = load_test_data()["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["email"] = unique_email
    
    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    
    id = response.json()["id"]
    responseget = api_client.get("users/10")
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()
    assert responseget.json()["name"] == "Clementina DuBuque"
    

def test_update_users(api_client):
    user_data = {
        "name": "Srikanth",
        "username": "srikanth",
        "email": "srikanth@example.com"
    }
    response = api_client.put("users/10", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == "Srikanth"
    

def test_delete_users(api_client):  
    
    response = api_client.delete("users/1")
    print(response.status_code)
    assert response.status_code == 200
   