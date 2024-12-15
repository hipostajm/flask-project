from sys import path
from flask import Flask
import pytest 
import json
path.append("")
from app.__unit__ import __all__

def get_user_by_id(l: list[object], id: int):
    try:
        return [obj for obj in l if obj["id"] == id][0]
    except:
        return None

@pytest.fixture
def client():
    return __all__["app"].test_client()

def test_users_get(client):
    assert json.loads(client.get("/users").data.decode()) == __all__["file"]

def test_users_get_with_id(client):
    id = 1
    assert json.loads(client.get(f"/users/{id}").data.decode()) == get_user_by_id(__all__["file"],id)

def test_users_get_with_out_of_range_id(client):
    id = len(__all__["file"])+1
    assert client.get(f"/users/{id}").status_code == 500

def test_users_post(client):
    name = 'woah'
    lastname = 'woah'
    id = len(__all__["file"])+1
    response = client.post("/users", json={'name': name, 'lastname': lastname})
    assert response.status_code == 201 and {"id":id,"name": name, "lastname": lastname} == get_user_by_id(__all__["file"],id)

def test_users_patch_with_name(client):
    id = 1
    value = "Imie"
    response = client.patch(f"/users/{id}", json={"name": value})
    assert response.status_code == 204 and value == get_user_by_id(__all__["file"],id)["name"]

def test_users_patch_with_lastname(client):
    id = 1
    value = "Nazwisko"
    response = client.patch(f"/users/{id}", json={"lastname": value})
    assert response.status_code == 204 and value == get_user_by_id(__all__["file"],id)["lastname"]

def test_users_patch_with_bad_data(client):
    id = 1
    value = "Imie"
    response = client.patch(f"/users/{id}", json={"Woah": value})
    assert response.status_code == 400

def test_users_put(client):
    id = 1
    name = "Imie"
    lastname = "Nazwisko"
    response = client.put(f"/users/{id}", json={"name": name, "lastname": lastname})
    assert response.status_code == 204 and get_user_by_id(__all__["file"],id) == {"id": id, "name": name, "lastname": lastname}

def test_users_delete_with_existing_user(client):
    id = 1
    response = client.delete(f"/users/{id}")
    assert response.status_code == 204
    
def test_users_delete_with_non_existing_user(client):
    id = 10000
    response = client.delete(f"/users/{id}")
    assert response.status_code == 400