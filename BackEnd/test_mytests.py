import pytest
import requests

from BackEnd import flaskAppInstance
from BackEnd import models
from BackEnd import db

test_url = 'http://localhost:8000'

def test_getList():
    r1 = requests.get(url+'/posts')
    assert r1.status_code == 200

def test_get_individuals():
    r2 = requests.get(url+'/posts/69')
    assert r3.status_code == 200





