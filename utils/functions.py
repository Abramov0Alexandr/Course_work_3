import time
import requests
from operator import itemgetter


def json_reader() -> list:

    response = requests.get('https://api.npoint.io/27390f0e02c8539a928e')
    result = response.json()
    return result
