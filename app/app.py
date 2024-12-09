from flask import Flask, redirect
import json

file = {}
with open("../data/users.json", 'r') as file:
    file = json.load(file)

app = Flask(__name__)


@app.get("/")
def main():
    return redirect('/users')


@app.get("/users")
@app.route("/users/<id>", methods = ['GET'])
def users(id: int = None):
    return file if id is None else ([obj for obj in file if obj["id"] == int(id)][0])
        
@app.post("/users")
def post_useres():
    ...