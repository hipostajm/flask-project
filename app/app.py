from flask import Flask, redirect, request, Response
import json

with open("./app/users.json", 'r') as file:
    file = json.load(file)

free_ids = []

app = Flask(__name__)

@app.get("/users")
@app.route("/users/<id>", methods = ['GET'])
def users(id: int = None):
    return file if id is None else ([obj for obj in file if obj["id"] == int(id)][0])
        
@app.post("/users")
def post_useres():
    data = request.get_json()
    id = free_ids.sort()[0] if free_ids else len(file)+1
    file.append({'id': id, 'name': data["name"], 'lastname': data["lastname"]})
    return Response(status=201)

def value_change_in_file(keys: list|tuple, data: dict, id: int) -> Response:
    i = 0
    for obj in file:
        if obj["id"] == id:
            for key in keys:
                obj[key] = data[key]
            return Response(status=204)
        else:
            i += 1
    if i == len(file):
        return Response(status=400) 

@app.route("/users/<id>", methods = ['PATCH'])
def patch_users(id: int):
    data: dict = request.get_json()
    id = int(id)
    try:   
        return value_change_in_file(("name",), data, id) 
    except:
        pass
    try:
        return value_change_in_file(("lastname",), data, id) 
    except:
        return Response(status=400)

@app.route("/users/<id>", methods=["PUT"])
def put_users(id):
    data: dict = request.get_json()
    if int(id) in [obj["id"] for obj in file]:
        return value_change_in_file(("name","lastname"), data, int(id))
    else:
        file.append({"id": id, "name": data["name"], "lastname": data["lastname"]})
        return Response(status=204)

@app.route("/users/<id>", methods=["DELETE"])
def delete_users(id: int):
    id = int(id)
            
    for i, obj in enumerate(file):
        if obj["id"] == id:
            del file[i]
            return Response(status=204)
    
    return Response(status=400)
