from sys import path
from flask import Flask
import pytest 
import json
path.append("")
from app.__unit__ import __all__

def test_get_with_out_id():
    id = 1
    value = [{"id": id, "name": "Imie", "lastname": "nazwisko"}]
    __all__["setter"](value)
    assert __all__["get"]() == value

def test_get_with_id():
    id = 1
    value = [{"id": id, "name": "Imie", "lastname": "nazwisko"}]
    __all__["setter"](value)
    assert __all__["get"](id) == value[0]

def test_delete():
    id = 1
    value = [{"id": id, "name": "Imie", "lastname": "nazwisko"}]
    __all__['setter'](value)
    __all__['delete'](id)
    assert __all__["getter"]() == []