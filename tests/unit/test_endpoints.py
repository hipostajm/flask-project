from sys import path
path.append("")
from app.__unit__ import __all__

def test_get():
    id = 1
    value = [{"id": id, "name": "Imie", "lastname": "nazwisko"}]
    __all__["set"](value)
    assert __all__["get"]() == value

def test_get_with_id():
    id = 1
    value = [{"id": id, "name": "Imie", "lastname": "nazwisko"}]
    __all__["set"](value)
    assert __all__["get"](id) == value[0]