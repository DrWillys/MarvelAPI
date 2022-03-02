import requests
import sys


def make_get_request(url, payload):
    try:
        return requests.get(url, payload)
    except requests.ConnectionError:
        print("Cant connect to server")
        sys.exit()
